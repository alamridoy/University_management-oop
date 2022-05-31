from .uniperson import Uniperson

class Student(Uniperson):
    def __init__(self, name, id, contact, blood,department,account,studentId,guardian,exams,fee ) -> None:
        super().__init__(name, id, contact, blood,department,account)
        self.studentId = studentId
        self.guardian = guardian
        self.exams = []
        self.fee = 0

    def __str__(self) -> str:
        pts = super().__str__()
        return (f'{pts}, Student ID: {self.studentId}, Guardian: {self.guardian}, Exams:{self.exams}, Fee: {self.fee}')