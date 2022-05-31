from .person import Person

class Guardian(Person):
  def __init__(self,name, id, contact, blood,profession,income) -> None:
      super().__init__(name, id, contact, blood)
      self.profession = profession
      self.income = income


  def __str__(self) -> str:
        pts = super().__str__()
        return (f' {pts} , Profession: {self.profession},Income: {self.income}') 

         
    