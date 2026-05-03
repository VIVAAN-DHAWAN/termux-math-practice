# Termux Math Practice

A simple Python script to generate random quadratic equation problems for daily practice, aimed at Class 10 students preparing for exams.

## Features

- Generates random quadratic equations (ax^2 + bx + c = 0) with integer coefficients.
- Prompts the user to enter the roots (real or complex).
- Provides immediate feedback and tracks correct/incorrect answers.
- Saves session statistics to a local JSON file for progress monitoring.
- Lightweight and runs entirely in Termux on Android.

## How to Use

1. Ensure you have Python 3 installed (`pkg install python` in Termux).
2. Clone or download this repository.
3. Run the script:
   ```bash
   python3 math_practice.py
   ```
4. Follow the on-screen prompts. Type `exit` to quit and see your session summary.

## Example

```
$ python3 math_practice.py
Quadratic Practice - Enter roots as comma-separated values (e.g., 2, -3) or 'complex' for complex roots.
Type 'exit' to quit.

Problem 1: 2x^2 - 5x + 2 = 0
Your answer: 0.5, 2
Correct! 🎯

Problem 2: x^2 + 4x + 5 = 0
Your answer: complex
Correct! 🎯

...

Session complete. You solved 8 out of 10 correctly.
```

## Customization

- Adjust difficulty by editing the coefficient ranges in `math_practice.py`.
- Change the number of problems per session by modifying `NUM_PROBLEMS`.

## License

MIT – feel free to fork and adapt.
