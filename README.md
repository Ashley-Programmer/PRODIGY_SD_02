# Number Guessing Game 🎯

A simple and interactive web-based number guessing game built with HTML, CSS, and JavaScript. Challenge yourself to guess the computer's secret number between 1 and 100!

## 🎮 Game Features

- **Random Number Generation**: Computer generates a random number between 1-100
- **Interactive Feedback**: Get hints whether your guess is too high or too low
- **Attempt Tracking**: Keep track of how many attempts you've made
- **Input Validation**: Ensures only valid numbers between 1-100 are accepted
- **Keyboard Support**: Press Enter to submit your guess
- **Game Reset**: Start a new game anytime with the reset button
- **Responsive Design**: Works on desktop and mobile devices

## 📁 Project Structure

```
PRODIGY_SD_02/
├── index.html          # HTML file
├── style.css           # Styling
├── guess-game.js       # Game logic and functionality
└── README.md           # Project documentation
```

## 🛠️ Technologies Used

- **HTML5**: Structure and layout
- **CSS3**: Styling and responsive design
- **JavaScript (ES6)**: Game logic and interactivity

## 🎯 How to Play

1. The computer will generate a random number between 1 and 100
2. Enter your guess in the input field
3. Click "Submit" or press Enter to submit your guess
4. The game will tell you if your guess is:
   - **Too High**: Your guess is greater than the secret number
   - **Too Low**: Your guess is less than the secret number
   - **Correct**: Congratulations! You've guessed the number!
5. Keep track of your attempts and try to guess in as few tries as possible
6. Click "Reset Game" to start over with a new random number

## 🚀 Getting Started

### Prerequisites

- A modern web browser (Chrome, Firefox, Safari, Edge)
- No additional installations required!

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ashley-Programmer/PRODIGY_SD_02.git
   ```

2. **Navigate to the project directory**
   ```bash
   cd PRODIGY_SD_02
   ```

3. **Open the game**
   - Double-click `index.html` to open in your browser
   - Or right-click and select "Open with" → your preferred browser
   - Or use a local server for better development experience

### Using Live Server (Optional)

For development purposes, you can use Live Server:

```bash
# If you have Live Server extension in VS Code
# Right-click on index.html and select "Open with Live Server"

# Or use Python's built-in server
python -m http.server 8000
# Then open http://localhost:8000 in your browser
```

## 🎮 Game Rules

- **Range**: Numbers are between 1 and 100 (inclusive)
- **Input Validation**: Only integers within the valid range are accepted
- **Unlimited Attempts**: No limit on the number of guesses
- **Instant Feedback**: Get immediate hints after each guess

## 🔧 Code Highlights

### Key JavaScript Features

- **Random Number Generation**: `Math.floor(Math.random() * 100) + 1`
- **Input Validation**: Checks for NaN and range validation
- **Event Listeners**: Handles button clicks and keyboard events
- **DOM Manipulation**: Updates game state and user interface dynamically

### Game Logic Flow

1. Generate random number on game start
2. Capture and validate user input
3. Compare guess with target number
4. Provide feedback and update attempt counter
5. Handle game completion and reset functionality

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help improve the game:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Ideas for Enhancement

- Add difficulty levels (different number ranges)
- Implement a scoring system
- Add sound effects
- Create a leaderboard
- Add animations and visual effects
- Implement hints after certain number of attempts

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

- **Developer**: Ashley Koketso Motsie
- **Email**: motsieashley31@gmail.com
- **GitHub**: https://github.com/Ashley-Programmer

## 🙏 Acknowledgments

- Built as part of the Prodigy InfoTech internship program
- Inspired by classic number guessing games
- Thanks to the web development community for best practices and inspiration

---

**Enjoy the game and happy guessing! 🎉**