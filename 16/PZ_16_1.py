class Bank:
    money = 0
    rate = 0

    def add_percent(self):
        self.money += self.money * (self.rate / 100)

    def withdraw(self, amount):
        self.money -= amount


b = Bank()
b.money = 1000
b.rate = 10

b.add_percent()
b.withdraw(200)
print(b.money)


