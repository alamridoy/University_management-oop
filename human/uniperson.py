from .person import Person

class Uniperson(Person):
    def __init__(self, name, id, contact, blood,department,account) -> None:
        super().__init__(name, id, contact, blood)
        self.department = department
        self.account = account

    
    def __str__(self) -> str:
        pts = super().__str__()
        return (f' {pts} , Department: {self.department},Account: {self.account}') 
