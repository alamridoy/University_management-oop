class Address:
    def __init__(self,roadno,city,region,country,postalCode) -> None:
        self.roadno = roadno
        self.city = city
        self.region = region
        self.country = country
        self.postalCode = postalCode
        pass

    def __str__(self) -> str:
        return (f'Road NO:{self.roadno}, City:{self.city},Region: {self.region},Postal Code: {self.postalCode}')