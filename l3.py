class Bank():  # Let's create a bank, building ATMs
    crisis = False

    def create_atm(self):
        while not self.crisis:
            yield "$100"


hsbc = Bank()  # When everything's ok the ATM gives you as much as you want
corner_street_atm = hsbc.create_atm()
print(next(corner_street_atm))

a = (100 * q for q in range(10))
print(a)
print(next(a))
