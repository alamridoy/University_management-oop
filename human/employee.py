from .uniperson import Uniperson

class Employee(Uniperson):
    def __init__(self, name, id, contact, blood,employeeId,salary) -> None:
        super().__init__(name, id, contact, blood)
        self.employeeId = employeeId
        self.salary = salary

    def __str__(self) -> str:
        pts = super().__str__()
        return (f'{pts},EmployeeId : {self.employeeId} Salary : {self.salary}')