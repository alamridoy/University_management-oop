
from .employee import Employee

class Teacher(Employee):
    def __init__(self, name, id, contact, blood,employeeId,salary,subject) -> None:
        super().__init__(name, id, contact, blood)
        self.subject = subject

    def __str__(self) -> str:
        pts = super().__str__()
        return (f'{pts},Subject: {self.subject}')