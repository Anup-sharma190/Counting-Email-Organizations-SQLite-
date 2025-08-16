# Counting-Email-Organizations-SQLite-
This project is a beginner-friendly demonstration of Python + Databases, teaching how to:  Connect to SQLite  Create tables dynamically  Perform insert/update queries  Process unstructured text into structured data
# 📧 Email Domain Counter using SQLite

## 🔹 Project Overview
This project reads through an email log file (`mbox.txt`), extracts email domains, 
and counts how many times each domain appears. The results are stored in an SQLite 
database (`emaildb.sqlite`).  

It demonstrates:
- File handling in Python
- String manipulation (`split`)
- Database operations with `sqlite3`
- Insert/Update logic in relational databases

---

## 🔹 Features
- Reads any `.txt` email file (default: `mbox.txt`)
- Extracts **domain names** from email addresses
- Stores and updates domain counts inside **SQLite database**
- Demonstrates practical use of **Python + SQL integration**

---

## 🔹 Example Flow
1. User runs the script and enters file name (or press Enter for default `mbox.txt`)
2. Script processes lines starting with `From:`
3. Extracts email domain and updates the count
4. Commits results to `emaildb.sqlite`

---

## 🔹 Technologies Used
- **Python 3**
- **SQLite3**
- **File Handling**

---

## 🔹 Sample Output in Database
After running on `mbox.txt`, inside `emaildb.sqlite` → `Counts` table might look like:

| org             | count |
|-----------------|-------|
| umich.edu       | 536   |
| gmail.com       | 123   |
| iupui.edu       | 101   |
| caret.cam.ac.uk | 56    |

---

## 🔹 How to Run
```bash
python email_counter.py
Enter file name: mbox.txt
✅ Data committed to emaildb.sqlite successfully!
