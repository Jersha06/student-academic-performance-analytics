from pathlib import Path
import pandas as pd

class StudentDatabase:
    def __init__(self, data_dir="data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)

    def save_students(self, dataframe, filename="students.csv"):
        path = self.data_dir / filename
        dataframe.to_csv(path, index=False)
        return path

    def save_marks(self, dataframe, filename="marks.csv"):
        mark_cols = ["Student_ID", "Python", "Statistics", "Machine_Learning",
                     "Deep_Learning", "Database", "Data_Visualization"]
        path = self.data_dir / filename
        dataframe[mark_cols].to_csv(path, index=False)
        return path

    def load_students(self, filename="students.csv"):
        return pd.read_csv(self.data_dir / filename)

    def search(self, dataframe, student_id):
        return dataframe[dataframe["Student_ID"].astype(str).str.upper() == student_id.upper()]
