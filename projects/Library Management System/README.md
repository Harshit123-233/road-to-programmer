# 📚 Library Management System (CLI)

A command-line **Library Management System** built in Python to practice **Object-Oriented Programming (OOP)** and **Dataclasses**.

This project manages books and members using JSON as persistent storage and demonstrates how multiple objects interact with one another in a real-world application.

---

## ✨ Features

### 📖 Book Management
- Add new books
- Remove books
  - Individually
  - By author
  - By genre
- Search books by title
- View books
  - Alphabetically
  - Grouped by author
  - Grouped by genre
  - By availability

### 👤 Member Management
- Register new members
- Delete members
- View registered members
- Automatic one-year membership generation

### 🔄 Borrowing System
- Issue books to members
- Return borrowed books
- Prevent issuing unavailable books
- Restrict members to one borrowed book at a time

### 💾 Persistent Storage
- Stores books in `books.json`
- Stores members in `members.json`
- Automatically creates database files if they don't exist

---

## 🛠 Concepts Practiced

This project was built to strengthen my understanding of:

- Object-Oriented Programming (OOP)
- Dataclasses
- Classes & Objects
- Separation of Responsibilities
- JSON File Handling
- Object Serialization (Object ↔ Dictionary)
- Helper Functions
- Pathlib
- Exception Handling
- Data Validation
- Menu-driven CLI Design

---

## 📂 Project Structure

```text
Library Management System/
│
├── main.py
├── library_management.py
├── utils.py
├── database/
│   ├── books.json
│   └── members.json
└── README.md
```

---

## 🚀 How to Run

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd "Library Management System"
```

Run the program:

```bash
python main.py
```

---

## 📖 Learning Highlights

This project helped me understand:

- When to use a dataclass instead of a regular class
- How objects interact with one another
- Designing applications using multiple classes
- Keeping business logic separate from user interface code
- Converting objects to dictionaries for JSON storage and reconstructing them when loading data
- Structuring a medium-sized Python project

---

## 🔮 Future Improvements (Version 2)

Some ideas I plan to implement in the next version:

- Multiple copies of the same book
- Partial book search
- Book due dates
- Fine calculation for late returns
- Better input validation
- Password hashing
- SQL database support instead of JSON
- Reports and statistics
- ISBN support
- Improved search and filtering

---

## 📌 Note

This project was created primarily as a learning exercise to practice **Object-Oriented Programming** and **Dataclasses**, rather than to build a production-ready library management system.

---

## 👨‍💻 Author

Harshit

Learning Python one project at a time.