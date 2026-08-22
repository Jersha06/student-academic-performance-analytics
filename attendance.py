class AttendanceRecord:
    def __init__(self, student_id, attendance):
        self.student_id = student_id
        self.attendance = attendance

    def status(self):
        if self.attendance >= 85:
            return "Excellent"
        elif self.attendance >= 75:
            return "Good"
        elif self.attendance >= 65:
            return "Warning"
        return "Critical"

    def is_shortage(self):
        return self.attendance < 75
