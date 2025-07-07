class House:
    architect = "Robin Luther"
    house_created_count = 0

    def __init__(self, area, location, price):
        self.area = area
        self.location = location
        self.price = price
        House.house_created_count += 1

    def print_house_metadata(self):
        print(f"""
        House : 
        Design approved By {House.architect}
        Area : {self.area}
        Location: {self.location}
        Price: {self.price}
        Number: {House.house_created_count}
        """)

    # class method
    @classmethod
    def house_generic_data(cls):
        print(cls.architect)


for i in range(2352, 2389, 2):
    h1 = House(area=i * 3, location="Bangalore", price=i * 523)
    h1.print_house_metadata()
    House.house_generic_data()

