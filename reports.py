from pathlib import Path
import pandas as pd

class ReportGenerator:
    def __init__(self, dataframe, report_dir="reports"):
        self.df = dataframe
        self.report_dir = Path(report_dir)
        self.report_dir.mkdir(parents=True, exist_ok=True)

    def student_report(self, student_id):
        result = self.df[self.df["Student_ID"].astype(str).str.upper() == student_id.upper()]
        if result.empty:
            return None
        return result.T

    def top_students(self, n=10):
        return self.df.sort_values("Percentage", ascending=False).head(n)

    def export_csv(self, filename="student_report.csv"):
        path = self.report_dir / filename
        self.df.to_csv(path, index=False)
        return path

    def export_department_excel(self, filename="department_report.xlsx"):
        path = self.report_dir / filename
        dept = self.df.groupby("Department")["Percentage"].agg(
            Average="mean", Maximum="max", Minimum="min", Std_Dev="std"
        ).round(2)
        with pd.ExcelWriter(path, engine="openpyxl") as writer:
            self.df.to_excel(writer, sheet_name="Student Data", index=False)
            dept.to_excel(writer, sheet_name="Department Analysis")
        return path

    def export_all(self):
        return self.export_csv(), self.export_department_excel()
