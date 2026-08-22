import pandas as pd

class PandasAnalyzer:
    def __init__(self, dataframe):
        self.df = dataframe

    def summary(self):
        return self.df.describe(include="all")

    def department_analysis(self):
        return self.df.groupby("Department")["Percentage"].agg(
            ["mean", "max", "min", "std"]
        ).round(2)

    def gender_analysis(self):
        return self.df.groupby("Gender")["Percentage"].mean().round(2)

    def subject_average(self, subjects):
        return self.df[subjects].mean().round(2)

    def semester_analysis(self):
        return self.df.groupby(["Year", "Semester"])["Percentage"].mean().round(2)

    def pivot_gender_department(self):
        return pd.pivot_table(
            self.df,
            values="Percentage",
            index="Department",
            columns="Gender",
            aggfunc="mean"
        ).round(2)
