🔐 Caesar Cipher - Python Implementation

A simple and interactive Caesar Cipher encryption & decryption tool built using Python.

This project allows users to encode and decode messages using a shift value, while preserving spaces, numbers, and special characters.

🚀 Features

Encode text using a shift key

Decode text back to original form

Handles alphabet wrapping using modulo (%)

Preserves spaces, numbers, and symbols

Loop-based interface (can run multiple times)

Clean function-based implementation

Input sanitization using .strip() and .lower()

🧠 Concepts Used

Functions with parameters

Local vs Global variables

Loops (for, while)

Conditional statements

String manipulation

Modulo operator

Input handling & sanitization

📌 How It Works
Encoding

Each letter is shifted forward by the given shift amount.

Example:

pen + shift 3 → shq
Decoding

Each letter is shifted backward by the given shift amount.

Example:

shq - shift 3 → pen

Modulo operator ensures wrapping:

z + 3 → c
▶️ How to Run

Make sure Python is installed.

Run the script:

python caeser_cipher.py

Follow the prompts:

Type encode or decode

Enter your message

Enter shift value

Choose whether to restart

🎯 Learning Outcome

This project helped strengthen my understanding of:

Function design with parameters

Scope handling (local vs global variables)

Clean user input management

Basic encryption logic

📈 Future Improvements

Add uppercase letter support

Add error handling for invalid input

Add GUI version

Convert to a web app

👨‍💻 Author

Built as part of my Python learning journey 🚀
More projects coming soon!
