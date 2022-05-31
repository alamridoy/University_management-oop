class Exam:
    def __init__(self,name,passmark,subject) -> None:
        self.name = name
        self.passmark = passmark
        self.subject = subject
        pass


    def __str__(self) -> str:
        
        return (f'ExamName: {self.name},PassMark: {self.passmark},Subject:{self.subject}')