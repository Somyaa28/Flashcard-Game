from tkinter import *
import pandas as pd
import random

score = 0
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = []

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/Sheet1.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

show_answer_timer = None
with open("HS.txt") as HS:
    highest_score = int(HS.read())


def update_highest_score():
    global highest_score
    if score > highest_score:
        highest_score = score
        with open("HS.txt", mode='w') as HS:
            HS.write(f'{highest_score}')
        highest_score_label.config(text=f"Highest Score: {highest_score}")


def next_card():
    global current_card, flip_timer, show_answer_timer
    window.after_cancel(flip_timer)
    if show_answer_timer:
        window.after_cancel(show_answer_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Word", fill="black")
    canvas.itemconfig(card_word, text=current_card["Word"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(20000, func=flip_card)
    entry.delete(0, END)
    check_button["state"] = "normal"
    give_up_button["state"] = "normal"


def flip_card():
    canvas.itemconfig(card_title, text="Meaning", fill="white")
    canvas.itemconfig(card_word, text=current_card["Meaning"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
    check_button["state"] = "normal"
    give_up_button["state"] = "disabled"
    global show_answer_timer  # Declare show_answer_timer as global
    show_answer_timer = window.after(5000, func=next_card)


def check_answer():
    global score
    user_answer = entry.get().strip().lower()
    correct_answer = current_card["Meaning"].strip().lower()

    # Check if the stripped user's answer is equal to the stripped correct answer
    if user_answer == correct_answer:
        to_learn.remove(current_card)
        score += 1
        update_highest_score()
        data = pd.DataFrame(to_learn)
        data.to_csv("data/words_to_learn.csv", index=False)  # Correct the file name
        message_label.config(text=f"Correct! Your score: {score}")
        next_card()
    else:
        message_label.config(text="Try again!")


def give_up():
    canvas.itemconfig(card_title, text="Meaning", fill="white")
    canvas.itemconfig(card_word, text=current_card["Meaning"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
    check_button["state"] = "disabled"
    give_up_button["state"] = "disabled"
    global show_answer_timer  # Declare show_answer_timer as global
    show_answer_timer = window.after(5000, func=next_card)


window = Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f'{screen_width}x{screen_height}')
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(20000, func=flip_card)

canvas = Canvas(width=800, height=626)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 313, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 30, "bold"))
card_word = canvas.create_text(400, 313, text="", font=("Arial", 40, "normal"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

entry = Entry()
entry.grid(row=1, column=0, columnspan=2)
entry.focus()

check_button = Button(text="Check", command=check_answer, state="disabled", font=("Arial", 16))
check_button.grid(row=2, column=0, padx=10, pady=10)

give_up_button = Button(text="Give Up", command=give_up, state="disabled", font=("Arial", 16))
give_up_button.grid(row=2, column=1, padx=10, pady=10)

message_label = Label(text=f"Your score: {score}", font=("Arial", 12))
message_label.grid(row=3, column=0, columnspan=2, pady=(0, 0))  

highest_score_label = Label(text=f"Highest Score: {highest_score}", font=("Arial", 12))
highest_score_label.grid(row=0, column=1, sticky='ne')

next_card()

def exit_game():
    window.destroy()

exit_button = Button(text="Exit", command=exit_game, bg="red", fg="white")
exit_button.grid(row=4, column=0, columnspan=2, pady=(0, 0))  

window.mainloop()
