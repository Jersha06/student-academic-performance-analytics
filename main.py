from pathlib import Path
import numpy as np
import pandas as pd

from database import StudentDatabase
from numpy_analysis import NumPyAnalyzer
from pandas_analysis import PandasAnalyzer
from visualization import VisualizationManager
from reports import ReportGenerator
from utilities import configure_logging

SUBJECTS = [
    "Python", "Statistics", "Machine_Learning",
    "Deep_Learning", "Database", "Data_Visualization"
]

def generate_dataset(n=1000, seed=42):
    rng = np.random.default_rng(seed)
    departments = ["Data Science", "Computer Science", "Artificial Intelligence",
                   "Information Technology"]
    genders = ["Male", "Female", "Other"]
    rows = []

    for i in range(1, n + 1):
        marks = np.clip(rng.normal(70, 15, 6), 25, 100).round().astype(int)
        rows.append({
            "Student_ID": f"DS{i:04d}",
            "Name": f"Student_{i:04d}",
            "Gender": rng.choice(genders),
            "Department": rng.choice(departments),
            "Year": int(rng.integers(1, 3)),
            "Semester": int(rng.integers(1, 5)),
            "Age": int(rng.integers(20, 25)),
            "Attendance": round(float(np.clip(rng.normal(80, 12), 45, 100)), 2),
            "Python": marks[0],
            "Statistics": marks[1],
            "Machine_Learning": marks[2],
            "Deep_Learning": marks[3],
            "Database": marks[4],
            "Data_Visualization": marks[5],
            "Assignment_Score": int(np.clip(rng.normal(75, 15), 20, 100)),
            "Internal_Marks": int(np.clip(rng.normal(72, 15), 20, 100)),
            "Project_Marks": int(np.clip(rng.normal(75, 15), 20, 100)),
            "Study_Hours": round(float(np.clip(rng.normal(16, 7), 2, 40)), 1),
            "Placement_Status": rng.choice(["Placed", "Not Placed", "Internship"])
        })

    df = pd.DataFrame(rows)

    # Deliberate missing values, as required by the project specification.
    df.loc[5, "Python"] = np.nan
    df.loc[12, "Attendance"] = np.nan
    df.loc[20, "Study_Hours"] = np.nan

    return df

def clean_and_engineer(df):
    df = df.copy()
    for col in SUBJECTS + ["Attendance", "Study_Hours"]:
        df[col] = df[col].fillna(df[col].mean())

    df["Total_Marks"] = df[SUBJECTS].sum(axis=1)
    df["Percentage"] = df["Total_Marks"] / (len(SUBJECTS) * 100) * 100

    def grade(mark):
        if mark >= 90: return "A+"
        if mark >= 80: return "A"
        if mark >= 70: return "B"
        if mark >= 60: return "C"
        if mark >= 50: return "D"
        return "F"

    df["Grade"] = df["Percentage"].apply(grade)
    df["GPA"] = df["Percentage"].apply(
        lambda x: 10.0 if x >= 90 else 9.0 if x >= 80 else
                  8.0 if x >= 70 else 7.0 if x >= 60 else
                  6.0 if x >= 50 else 5.0
    )
    df["Rank"] = df["Percentage"].rank(ascending=False, method="dense").astype(int)

    def attendance_status(x):
        if x >= 85: return "Excellent"
        if x >= 75: return "Good"
        if x >= 65: return "Warning"
        return "Critical"

    df["Attendance_Status"] = df["Attendance"].apply(attendance_status)
    df["At_Risk"] = (
        (df["Attendance"] < 75) |
        (df["Percentage"] < 50) |
        (df["Study_Hours"] < 10) |
        (df[SUBJECTS].lt(50).any(axis=1))
    )

    df["Risk_Score"] = 0
    df.loc[df["Attendance"] < 75, "Risk_Score"] += 1
    df.loc[df["Percentage"] < 50, "Risk_Score"] += 2
    df.loc[df["Study_Hours"] < 10, "Risk_Score"] += 1
    df.loc[df[SUBJECTS].lt(50).any(axis=1), "Risk_Score"] += 1

    def risk_category(score):
        if score >= 3: return "High Risk"
        if score == 2: return "Medium Risk"
        if score == 1: return "Low Risk"
        return "Safe"

    df["Risk_Category"] = df["Risk_Score"].apply(risk_category)
    return df

def print_menu():
    print("\n==============================")
    print(" STUDENT ANALYTICS SYSTEM")
    print("==============================")
    print("1. Display Students")
    print("2. Show Top Students")
    print("3. Department Analysis")
    print("4. Subject Analysis")
    print("5. Attendance Analysis")
    print("6. At-Risk Students")
    print("7. Student Search")
    print("8. Overall Statistics")
    print("9. Export Reports")
    print("10. Generate Charts")
    print("11. Exit")

def main():
    configure_logging()
    print("Generating 1,000 synthetic student records...")
    df = clean_and_engineer(generate_dataset())

    db = StudentDatabase()
    db.save_students(df)
    db.save_marks(df)

    pandas_analyzer = PandasAnalyzer(df)
    report = ReportGenerator(df)
    viz = VisualizationManager(df)

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                print(df.head(20).to_string(index=False))
            elif choice == "2":
                print(report.top_students().to_string(index=False))
            elif choice == "3":
                print(pandas_analyzer.department_analysis())
            elif choice == "4":
                print(pandas_analyzer.subject_average(SUBJECTS))
            elif choice == "5":
                print(df["Attendance"].describe())
            elif choice == "6":
                print(df[df["At_Risk"]].to_string(index=False))
            elif choice == "7":
                sid = input("Enter Student ID: ").strip()
                result = report.student_report(sid)
                print("Student not found." if result is None else result.to_string(header=False))
            elif choice == "8":
                print(f"Average Percentage: {df['Percentage'].mean():.2f}")
                print(f"Highest Percentage: {df['Percentage'].max():.2f}")
                print(f"Lowest Percentage : {df['Percentage'].min():.2f}")
                print(f"Overall Pass %    : {(df['Percentage'] >= 50).mean() * 100:.2f}")
                print(f"At-Risk Students  : {df['At_Risk'].sum()}")
                marks = NumPyAnalyzer(df[SUBJECTS].to_numpy().ravel())
                print("NumPy Statistics  :", marks.statistics())
            elif choice == "9":
                print("Created:", report.export_all())
            elif choice == "10":
                viz.create_all()
                print("Charts generated in the charts/ folder.")
            elif choice == "11":
                print("Thank you!")
                break
            else:
                print("Invalid choice. Please enter 1-11.")
        except (ValueError, KeyError) as exc:
            print("Input/processing error:", exc)

if __name__ == "__main__":
    main()
