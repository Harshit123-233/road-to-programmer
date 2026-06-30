# 🔐 Signup & Login System (CLI)

A simple command-line based Signup and Login System built using Python.

This project was created as part of my **Road to Programmer** journey while learning Python fundamentals.

---

## 🚀 Features

- 📝 User Sign Up
- 🔑 User Login
- 💾 Stores user data in a JSON database
- 📂 Automatically creates the database if it does not exist
- ⚠️ Handles corrupted JSON files gracefully
- 🛡️ Uses exception handling for common errors
- 🚪 Exit option
- 👨‍💻 Hidden developer easter egg 👀

---

## 🛠️ Concepts Practiced

- Functions
- JSON (`json` module)
- File Handling
- Exception Handling (`try...except`)
- Modules (`os`)
- Loops
- Conditional Statements
- Dictionaries
- Lists

---

## 📁 Project Structure

```text
signup_login_system/
│
├── main.py          # Main application
├── db_users.json    # Stores user credentials
└── README.md
```

---

## ▶️ How to Run

1. Clone this repository.

2. Navigate to the project folder.

3. Run:

```bash
python main.py
```

---

## ⚠️ Note

This project stores passwords as **plain text** because it was built for learning purposes.

In a real-world application, passwords should always be hashed using libraries such as `bcrypt`.

---

## 📚 What I Learned

While building this project, I learned how to:

- Read and write JSON files
- Create files if they don't exist
- Handle common file-related exceptions
- Organize a project into separate files and folders
- Build a simple authentication flow

---

## 👨‍💻 Author

**Harshit**

This project is part of my **Road to Programmer** repository where I document my journey of becoming a software developer.

---

> Every project in this repository represents a milestone in my learning journey. Feedback and suggestions are always welcome!