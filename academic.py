class AcademicRecord:
    def __init__(self, student_id, marks):
        self.student_id = student_id
        self.marks = marks

    def total(self):
        return sum(self.marks.values())

    def average(self):
        return self.total() / len(self.marks)

    def highest(self):
        return max(self.marks.values())

    def lowest(self):
        return min(self.marks.values())

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        return "F"

    def gpa(self):
        avg = self.average()
        if avg >= 90: return 10.0
        if avg >= 80: return 9.0
        if avg >= 70: return 8.0
        if avg >= 60: return 7.0
        if avg >= 50: return 6.0
        return 5.0
