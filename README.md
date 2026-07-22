# 🎓 Student Management System

A simple Python-based **Student Management System** developed to demonstrate **Continuous Integration (CI)** using **Jenkins**.

---

## 📖 Overview

This project manages student records, calculates grades, and demonstrates how Jenkins automatically builds, tests, and validates code whenever changes are pushed to GitHub.

---

## ✨ Features

- Add and manage student records
- Calculate grades automatically
- Display student results in a formatted table
- Automated unit testing using **Pytest**
- Continuous Integration using **Jenkins Pipeline**
- Source code management with **Git & GitHub**

---

## 🛠 Technologies Used

- Python 3
- Pytest
- Git
- GitHub
- Jenkins

---

## 📁 Project Structure

```text
StudentManagementSystem/
│
├── src/
│   ├── main.py
│   ├── student.py
│   └── grading.py
│
├── tests/
│   └── test_grading.py
│
├── Jenkinsfile
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙ Jenkins Pipeline

The Jenkins pipeline performs the following steps automatically:

1. Checkout the latest code from GitHub
2. Install project dependencies
3. Run the Student Management System
4. Execute all unit tests using Pytest
5. Report the build status (Success or Failure)

---

## 🧪 Testing

The project includes automated unit tests for the grading system.

Example test cases:

- 95 → Grade A
- 85 → Grade B
- 75 → Grade C
- 65 → Grade D
- 40 → Grade F

---

## 🔄 Continuous Integration Demonstration

During development, an intentional bug was introduced into the grading logic.

Jenkins automatically:

- Detected the new commit
- Executed the test suite
- Reported the failed test
- Marked the build as **FAILED**

After fixing the bug and pushing the corrected code, Jenkins rebuilt the project and all tests passed successfully.

This demonstrates how Continuous Integration helps detect software defects before deployment.

---

## 👨‍💻 Author

**Rehman Gul**

Software Engineering Project