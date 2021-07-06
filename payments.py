
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
    pass

class Comission:
    pass

