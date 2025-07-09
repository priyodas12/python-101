class Bank:
    def __init__(self,name,origin):
        self.name=name
        self.origin=origin

    # utility method
    @staticmethod
    def get_interest_rate(current_year):
        print(f"Current Interest Rate:: {12500/((current_year-2000)*100)}")

bank= Bank('canara','india')
bank.get_interest_rate(2029)