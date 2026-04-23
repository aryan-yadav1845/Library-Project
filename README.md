# Library Management System 📚

A Python-based application designed to manage library operations, including inventory tracking, book issuance, and automated fine calculation.

## ✨ Features
- **Dictionary-Based Records:** Uses Python dictionaries to efficiently manage book quantities and student issue records.
- **Student Tracking:** Keeps track of who issued which book, the date, and the duration.
- **Tiered Fine System:** Automatically calculates penalties for late returns based on the following schedule:
  - **1st Week Late:** 10 Rs / day
  - **2nd Week Late:** 20 Rs / day (10 * 2)
  - **3rd Week Late:** 60 Rs / day (10 * 2 * 3)
  - *Multipliers continue to increase factorially for subsequent weeks.*
- **Improved UI:** Redesigned input and output statements for a better user experience.

## 🛠️ How to Run
1. Ensure you have Python installed.
2. Clone this repository or download the `library.py` file.
3. Run the script:
   ```bash
   python library.py
