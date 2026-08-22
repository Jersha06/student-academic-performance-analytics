from pathlib import Path
import matplotlib.pyplot as plt

class VisualizationManager:
    def __init__(self, dataframe, output_dir="charts"):
        self.df = dataframe
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def create_all(self):
        self.performance_distribution()
        self.department_performance()
        self.attendance_distribution()
        self.subject_performance()
        self.correlation_heatmap()

    def performance_distribution(self):
        plt.figure(figsize=(10, 6))
        plt.hist(self.df["Percentage"], bins=10)
        plt.xlabel("Percentage")
        plt.ylabel("Number of Students")
        plt.title("Distribution of Student Performance")
        plt.tight_layout()
        plt.savefig(self.output_dir / "performance.png")
        plt.close()

    def department_performance(self):
        avg = self.df.groupby("Department")["Percentage"].mean()
        plt.figure(figsize=(10, 6))
        avg.plot(kind="bar")
        plt.title("Average Performance by Department")
        plt.ylabel("Average Percentage")
        plt.tight_layout()
        plt.savefig(self.output_dir / "department_performance.png")
        plt.close()

    def attendance_distribution(self):
        plt.figure(figsize=(10, 6))
        plt.hist(self.df["Attendance"], bins=10)
        plt.xlabel("Attendance (%)")
        plt.ylabel("Number of Students")
        plt.title("Attendance Distribution")
        plt.tight_layout()
        plt.savefig(self.output_dir / "attendance.png")
        plt.close()

    def subject_performance(self):
        subjects = ["Python", "Statistics", "Machine_Learning",
                    "Deep_Learning", "Database", "Data_Visualization"]
        self.df[subjects].mean().plot(kind="bar", figsize=(10, 6))
        plt.title("Average Performance by Subject")
        plt.ylabel("Average Marks")
        plt.tight_layout()
        plt.savefig(self.output_dir / "subjects.png")
        plt.close()

    def correlation_heatmap(self):
        cols = ["Study_Hours", "Attendance", "Internal_Marks", "Percentage"]
        corr = self.df[cols].corr()
        plt.figure(figsize=(8, 6))
        plt.imshow(corr, interpolation="nearest")
        plt.colorbar()
        plt.xticks(range(len(cols)), cols, rotation=30, ha="right")
        plt.yticks(range(len(cols)), cols)
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        plt.savefig(self.output_dir / "correlation.png")
        plt.close()
