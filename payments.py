
class Hourly:
    
    def __init__(self):
        self.per_hour = int(input("Quanto por hora o funcionário vai receber: "))
        self.money = 0
        self.name_type = "Horista"
        self.payment_agenda = "semanalmente"

    def time_cards(self, hours_worked):
        if hours_worked > 8:
            self.money += (self.per_hour*8) + 1.5*self.per_hour*(hours_worked-8)
        else:
            self.money = self.per_hour*hours_worked
        
        print(self.money)

    def paid(self):
        value = self.money
        self.money = 0
        return value

class Month:
    
    def __init__(self):
        self.salary = int(input("Quanto vai ser o salário do funcionário: "))
        self.money = self.salary
        self.name_type = "Mensal"
        self.payment_agenda = "mensalmente"

    def paid(self):
        value = self.money
        return value

class Comission:
    
    def __init__(self):
        self.salary = int(input("Quanto vai ser o salário do funcionário: "))
        self.comission_percent = int(input("Quanto vai ser a comissão do funcionário: "))/100
        self.money = self.salary
        self.name_type = "Comissionado"
        self.payment_agenda = "bi-semanalmente"
    
    def sell_results(self, value):
        self.money += (self.comission_percent*value)

    def paid(self):
        value = self.money
        self.money = self.salary
        return value
