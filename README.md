# 🗄️ SQL Kickstart – dvdrental PostgreSQL Exercises

> A complete PostgreSQL SQL practice repository containing **15 hands-on exercises** covering SQL fundamentals to intermediate concepts, along with a **Python automation script** that exports query results into Excel.

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16+-336791?logo=postgresql\&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python\&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📖 About

This repository contains solutions to **15 SQL exercises** built on the famous **dvdrental PostgreSQL database**.

The exercises gradually progress from beginner topics such as **SELECT** and **WHERE** to advanced concepts including:

* Joins
* Window Functions
* CTEs
* Views
* Materialized Views
* Temporary Tables
* Python Automation

The final exercise automates all SQL queries using **Python**, **psycopg2**, and **openpyxl**, exporting every query result into a single Excel workbook.

---

# 🛠 Tech Stack

* PostgreSQL
* dvdrental Database
* Python 3
* psycopg2
* openpyxl
* VS Code

---

# 📚 Topics Covered

| #  | Topic                      | Concept                   |
| -- | -------------------------- | ------------------------- |
| 1  | First Look at the Catalog  | SELECT, Alias, LIMIT      |
| 2  | The A-List, Just Right     | WHERE, BETWEEN, LIKE      |
| 3  | Rating Breakdown           | GROUP BY, COUNT           |
| 4  | The Crowded Shelves        | HAVING                    |
| 5  | What Genre Is That Film?   | INNER JOIN                |
| 6  | Clean Up the Customer List | String Functions          |
| 7  | One Directory              | UNION ALL                 |
| 8  | Length of Film?            | CASE Statements           |
| 9  | The Big Spenders           | CTE (WITH Clause)         |
| 10 | Pricier Than Average       | Subqueries                |
| 11 | Top Films in Each Genre    | Window Functions          |
| 12 | A Reusable Film Catalog    | Views                     |
| 13 | Cached Revenue by Category | Materialized Views        |
| 14 | Stage the Top 10           | Temporary Tables          |
| 15 | Automate Everything        | Python + psycopg2 + Excel |

---

# 📂 Project Structure

```text
SQL-Kickstart/
│
├── Exercise_01/
├── Exercise_02/
├── Exercise_03/
├── Exercise_04/
├── Exercise_05/
├── Exercise_06/
├── Exercise_07/
├── Exercise_08/
├── Exercise_09/
├── Exercise_10/
├── Exercise_11/
├── Exercise_12/
├── Exercise_13/
├── Exercise_14/
├── Exercise_15/
│   ├── main.py
│   ├── requirements.txt
│   └── sql_exercise_outputs.xlsx
│
├── README.md
└── LICENSE
```


# ⚡ Running the Project

## 1. Clone Repository

```bash
git clone https://github.com/<your-username>/<your-repository>.git
```

```bash
cd <your-repository>
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Configure Database

Update your PostgreSQL connection details in `main.py`.

```python
DB_CONFIG = {
    "host": "localhost",
    "database": "dvdrental",
    "user": "postgres",
    "password": "YOUR_PASSWORD",
    "port": 5432
}
```

---

## 4. Run the Automation Script

```bash
python main.py
```

---

# 📊 Output

The automation script generates:

```text
sql_exercise_outputs.xlsx
```

Workbook Structure

```text
📄 sql_exercise_outputs.xlsx

├── Q1
├── Q2
├── Q3
├── Q4
├── Q5
├── Q6
├── Q7
├── Q8
├── Q9
├── Q10
├── Q11
├── Q12
├── Q13
└── Q14
```

Each worksheet contains:

* Column headers
* Query results
* Automatically generated Excel sheet

---

# 🎯 Learning Outcomes

After completing this project, you will be comfortable with:

* SQL Fundamentals
* Filtering & Sorting
* Aggregations
* HAVING
* Multi-table Joins
* String Functions
* UNION & UNION ALL
* CASE Statements
* Common Table Expressions
* Subqueries
* Window Functions
* Views
* Materialized Views
* Temporary Tables
* Python Database Programming
* Excel Report Automation

---


---



If you found this project helpful, consider giving it a ⭐ on GitHub!
