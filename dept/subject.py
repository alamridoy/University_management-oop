class Subject:
    def __init__(self,name,credit) -> None:
        self.name = name
        self.credit = credit
        pass


    def __str__(self) -> str:
        
        return (f'ExamName: {self.name} Credit: {self.credit}')