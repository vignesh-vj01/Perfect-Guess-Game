# 🎯 The Perfect Guess Game

A simple **Python-based number guessing game** where the player has to guess a randomly generated number between **1 and 100**.  
The game provides hints after each guess and lets you **play multiple rounds** without restarting the program.

---

## 📜 Features
- Random number generation between **1–100**.
- Unlimited guesses until the correct number is found.
- Hints after each guess:
  - `"Your guess is too low."`
  - `"Your guess is too high."`
- Input validation to handle invalid or out-of-range guesses.
- Option to **play again** without restarting the script.

---

## 🛠 Requirements
- Python 3.x  
(No external libraries are required.)

---

## 🚀 How to Run

1. **Clone or download** the repository.
2. Open a terminal in the project directory.
3. Run the script:
   ```bash
   python main.py

## 🎮 How to Play
- The game will select a random number between 1 and 100.
- Enter your guess.
- The game will tell you if your guess is too high or too low.
- Keep guessing until you find the correct number.
- After each round, you can choose to play again.

📂 Project Structure
 ```
 Perfect-Guess-Game/
 │
 ├── main.py   # Main game script
 └── README.md               # Project documentation
 ```

## 💡 Example Gameplay
```
************** Welcome to The Perfect Guess Game! **************
I have selected a number between 1 and 100. Can you guess it?
Enter your guess between 1 and 100: 50
📈 Your guess is too high. Try again.
Enter your guess between 1 and 100: 25
📉 Your guess is too low. Try again.
Enter your guess between 1 and 100: 37
🎉 Congratulations! You've guessed the number 37 in 3 attempts.

Do you want to play again? (y/n): y
```

## 🏆 Future Enhancements
- Track and display the best score across rounds.
- Add difficulty levels (Easy, Medium, Hard).
- Add colorized output for better readability.

## 📄 License
This project is open-source and available under the MIT License.
