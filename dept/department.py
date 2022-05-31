class Department:
    def __init__(self,name,subjects,dean,teachers) -> None:
        self.name = name
        self.subjects = []
        self.dean = dean
        self.teachers = []
        pass


    def __str__(self) -> str:
        
        return (f'DepartmentName: {self.name}, Subjects: {self.subjects},Dean: {self.dean},Teachers: {self.teachers}')