# Student Academic Performance & Analytics Management System

A Python-based MSc-level academic analytics project using OOP, NumPy, Pandas, Matplotlib, CSV and Excel reporting.

## Features

- 1,000 synthetic student records
- Student and academic management
- Attendance analysis
- GPA, percentage and grade calculation
- Student ranking
- At-risk student identification and risk scoring
- NumPy statistical analysis
- Pandas filtering/grouping/aggregation
- Department, gender, subject and semester analysis
- Five visualizations
- CSV and Excel export
- Menu-driven interface
- Exception handling and logging
- Multiple Python modules demonstrating OOP structure

## Project Structure

```text
student_analytics/
├── main.py
├── student.py
├── academic.py
├── attendance.py
├── database.py
├── numpy_analysis.py
├── pandas_analysis.py
├── visualization.py
├── reports.py
├── utilities.py
├── requirements.txt
├── README.md
├── data/
│   ├── students.csv
│   └── marks.csv
├── reports/
│   ├── student_report.csv
│   └── department_report.xlsx
├── charts/
│   ├── performance.png
│   ├── department_performance.png
│   ├── attendance.png
│   ├── subjects.png
│   └── correlation.png
└── logs/
    └── application.log
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

The application regenerates the dataset, cleans it, creates engineered features, exports the data/reports and provides a menu-driven interface.

## Notes

The project follows the supplied project specification. It includes deliberate missing values and cleans them before analysis. The generated dataset is synthetic and intended for academic/laboratory use.
