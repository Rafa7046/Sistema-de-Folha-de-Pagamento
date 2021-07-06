
class Hourly:
    
    def __init__(self):
        self.per_hour = int(input("Quanto por hora o funcionário vai receber: "))
        self.money = 0

    def time_cards(self, hours_worked):
        if hours_worked > 8:
            self.money += (self.per_hour*8) + 1.5*self.per_hour*(hours_worked-8)
        else:
            self.money = self.per_hour*hours_worked
        
        print(self.money)

class Month:
    
    def __init__(self):
        self.salary = int(input("Quanto vai ser o salário do funcionário: "))
        self.money = 0

class Comission:
    
    def __init__(self):
        self.salary = int(input("Quanto vai ser o salário do funcionário: "))
        self.comission_percent = int(input("Quanto vai ser a comissão do funcionário: "))/100
        self.money = 0
    
    def sell_results(self, value):
        self.money += (self.comission_percent*value)
