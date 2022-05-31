class Person:
    def __init__(self,name,id,contact,blood) -> None:
        self.name = name
        self.id = id
        self.contact = contact
        self.blood = blood

    def log(self):
        print(self.__dict__)

    def __str__(self) -> str:
        return (f'Name: {self.name} , Id: {self.id}, Contact: {self.contact} , Blood Group: {self.blood}')