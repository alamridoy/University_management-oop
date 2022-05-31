

class Contact:
    def __init__(self,email,phone,address) -> None:
        self.email = email
        self.phone = phone
        self.address = address
        pass


    def __str__(self) -> str:
        add  = self.address.__str__()
        return (f'Email: {self.email},Phone: {self.phone},Address:{add}')