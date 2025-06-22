const guess_input = document.getElementById('guess-input');
const submit_btn = document.getElementById('submit-btn');
const message = document.getElementById('message');
const attempts_display = document.getElementById('attempts');
const restart_btn = document.getElementById('restart-btn');

let random_number = Math.floor(Math.random() * 100) + 1;
let attempts = 0;

submit_btn.addEventListener('click', () => {
    const guess = parseInt(guess_input.value);
    attempts++;

    if (isNaN(guess) || guess < 1 || guess > 100) {
        message.textContent = "Enter an integer number between 1 and 100!";
        return;
    }
    if (guess === random_number) {
        message.textContent = `Correct! The number was ${random_number}`;
        submit_btn.disabled = true;
        restart_btn.style.display = "inline-block";
    } else if (guess < random_number) {
        message.textContent = "Too low! try again.";
    } else {
        message.textContent = "Too high! try again.";
    }

    attempts_display.textContent = `Attempts: ${attempts}`;
});

restart_btn.addEventListener('click', () => {
    random_number = Math.floor(Math.random() * 100) + 1;
    attempts = 0;
    message.textContent = "";
    attempts_display.textContent = 'Attempts: 0';
    submit_btn.disabled = true;
    guess_input.value = '';
    restart_btn.style.display = 'none';
});

guess_input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
        submit_btn.click();
    }
});