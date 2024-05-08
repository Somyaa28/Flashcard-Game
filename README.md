# Flashcard Game

## Introduction
The Flashcard Game is a simple yet engaging application designed to help users learn and test their knowledge of words and their meanings. It provides a fun and interactive way to study vocabulary, improve memory retention, and enhance language skills.

## Features
- *Flashcards*: Display words on one side and their corresponding meanings on the other side of the card.
- *Check Answer*: Allows users to input their answer and check if it matches the correct meaning of the word.
- *Give Up*: Provides an option to reveal the correct answer if the user is unable to guess it.
- *Score Tracking*: Keeps track of the user's score and displays it during the game.
- *Highest Score*: Records and displays the highest score achieved by the user.
- *Data Persistence*: Saves progress and words to learn in a CSV file, allowing users to continue from where they left off.

## Installation
1. Clone or download the repository to your local machine.
2. Ensure you have Python installed.
3. Install the required dependencies by running pip install -r requirements.txt.
4. Run the flashcard_game.py file to start the application.

## Usage
1. Upon launching the application, a random flashcard will be displayed with the word on one side and a blank space on the other.
2. Input your answer in the provided entry field and click on the "Check" button to verify.
3. If you're unable to guess the answer, you can click on the "Give Up" button to reveal the correct meaning.
4. Your score will be updated based on correct answers, and the highest score achieved will be displayed.
5. Click on the "Exit" button to close the application.

## Data Management
- The application uses CSV files to store words to learn and the user's progress.
- If a words_to_learn.csv file exists, the application will load words from it; otherwise, it will use the default words provided in Sheet1.csv.
- Progress is automatically saved when the user exits the application.

## Contributors
- [Vanshika Verma]
- [Somya Agarwal]


## Conclusion

The Flashcard Game presents a dynamic and interactive approach to learning vocabulary and testing one's understanding of word meanings. With its user-friendly interface and engaging features, it offers a convenient way for users to enhance their language skills while having fun.

Throughout the development of this project, key functionalities such as displaying flashcards, checking answers, and tracking scores were implemented using Python and Tkinter. The integration of data persistence ensures that users can pick up from where they left off, promoting continuity in learning.

The Flashcard Game not only serves as a valuable educational tool but also fosters a sense of accomplishment as users progress through the game and strive to achieve their highest score. It encourages active participation and provides instant feedback, facilitating effective learning and retention of knowledge.

Overall, the Flashcard Game represents a successful endeavor in leveraging technology to facilitate learning and skill development. With its versatility and potential for further expansion, it holds promise as a versatile tool for learners of all ages and proficiency levels.