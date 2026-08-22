import numpy as np

class NumPyAnalyzer:
    def __init__(self, marks):
        self.marks = np.asarray(marks, dtype=float)

    def mean(self):
        return np.mean(self.marks)

    def median(self):
        return np.median(self.marks)

    def standard_deviation(self):
        return np.std(self.marks)

    def variance(self):
        return np.var(self.marks)

    def percentile(self, value):
        return np.percentile(self.marks, value)

    def statistics(self):
        return {
            "Mean": self.mean(),
            "Median": self.median(),
            "Standard Deviation": self.standard_deviation(),
            "Variance": self.variance(),
            "25th Percentile": self.percentile(25),
            "75th Percentile": self.percentile(75),
        }

    @staticmethod
    def correlation_matrix(values):
        return np.corrcoef(np.asarray(values, dtype=float).T)
