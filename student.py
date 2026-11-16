from dataclasses import dataclass, asdict
from datetime import date

@dataclass
class Student:
    student_id: str
    full_name: str
    class_form: str
    gender: str
    date_of_birth: str
    scores: dict

    @classmethod
    def from_dict(cls, data):
        return cls(
            student_id=data["student_id"],
            full_name=data["full_name"],
            class_form=data["class_form"],
            gender=data["gender"],
            date_of_birth=data["date_of_birth"],
            scores=data.get("scores", {})
        )

    def to_dict(self):
        return asdict(self)

    def add_or_update_score(self, subject, score):
        self.scores[subject] = {
            "score": float(score),
            "date_entered": date.today().isoformat()
        }
