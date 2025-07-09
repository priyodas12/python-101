class Bank:
    def __init__(self,name,origin,current_interest_rate):
        self.name=name
        self.origin=origin
        self.interest_rate=current_interest_rate

    def set_interest_rate(self,interest_rate):
        if  (not isinstance(interest_rate,float)) or (interest_rate<0.0):
            print("invalid interest rate passed!")
            raise ValueError("invalid value of interest passed")
        else:
            self.interest_rate = interest_rate

    def get_interest_rate(self):
        return self.interest_rate

    def __str__(self):
        print(f"Bank Name :: {self.name}, Origin:: {self.origin} ,Current Interest Rate :: {self.interest_rate}")

bank= Bank('canara','india',7.29)
#bank.set_interest_rate(-7.89) will throw exception here
bank.set_interest_rate(7.89)
print(f"current interest rate:: {bank.get_interest_rate()}")
bank.__str__()