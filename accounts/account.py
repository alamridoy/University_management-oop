class Account:
    def __init__(self,id,type,amount,time) -> None:
        self.id = id
        self.type = type
        self.amount = amount
        self.time = time
        pass

    def __str__(self) -> str:
        return (f'ID: {self.id},Type: {self.type},Amount: {self.type}, Time:{self.time}')