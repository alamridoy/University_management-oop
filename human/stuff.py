from .employee import Employee

class Stuff(Employee):
    def __init__(self, name, id, contact, blood,employeeId,salary,title) -> None:
        super().__init__(name, id, contact, blood)
        self.title = title

    def __str__(self) -> str:
        pts = super().__str__()
        return (f'{pts},Title: {self.title}')