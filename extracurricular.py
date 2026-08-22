from utilities import validate_non_empty_string, validate_range


class ExtracurricularRecord:

    ACTIVITY_FIELDS = ("Extracurricular_Score", "Outreach_Score", "Club_Activity_Score")

    def __init__(self, student_id, extracurricular_score, outreach_score,
                 club_activity_score):
        self.student_id = student_id
        self.extracurricular_score = extracurricular_score
        self.outreach_score = outreach_score
        self.club_activity_score = club_activity_score

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = validate_non_empty_string(value, "Student_ID")

    @property
    def extracurricular_score(self):
        return self._extracurricular_score

    @extracurricular_score.setter
    def extracurricular_score(self, value):
        self._extracurricular_score = validate_range(value, "Extracurricular_Score", 0, 100)

    @property
    def outreach_score(self):
        return self._outreach_score

    @outreach_score.setter
    def outreach_score(self, value):
        self._outreach_score = validate_range(value, "Outreach_Score", 0, 100)

    @property
    def club_activity_score(self):
        return self._club_activity_score

    @club_activity_score.setter
    def club_activity_score(self, value):
        self._club_activity_score = validate_range(value, "Club_Activity_Score", 0, 100)

    def overall_score(self):
        """Simple average across the three co-curricular dimensions."""
        return (self.extracurricular_score + self.outreach_score
                + self.club_activity_score) / 3

    def category(self):
        """Bucket overall engagement into a readable category."""
        score = self.overall_score()
        if score >= 85:
            return "Highly Active"
        elif score >= 70:
            return "Active"
        elif score >= 50:
            return "Moderately Active"
        return "Inactive"

    def strongest_area(self):
        areas = {
            "Extracurricular": self.extracurricular_score,
            "Outreach": self.outreach_score,
            "Club Activity": self.club_activity_score,
        }
        return max(areas, key=areas.get)

    def summary(self):
        return {
            "Student_ID": self.student_id,
            "Extracurricular_Score": round(self.extracurricular_score, 2),
            "Outreach_Score": round(self.outreach_score, 2),
            "Club_Activity_Score": round(self.club_activity_score, 2),
            "Co_Curricular_Score": round(self.overall_score(), 2),
            "Category": self.category(),
            "Strongest_Area": self.strongest_area(),
        }

    def __repr__(self):
        return (f"ExtracurricularRecord(student_id={self.student_id!r}, "
                f"overall={self.overall_score():.1f}, category={self.category()!r})")
