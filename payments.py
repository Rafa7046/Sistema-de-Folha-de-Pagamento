from employee import Employee

class Hourly(Employee):
    
    def __init__(self, name, address,type_of_payment, syndicate, Id, per_hour_prev=0):
        try:
            super().__init__(name, address,type_of_payment, syndicate, Id, syndicate.Id, syndicate.syndicate_fee, syndicate.total_fee)
        except:
            super().__init__(name, address,type_of_payment, syndicate, Id)
        if not per_hour_prev:
            self.per_hour = int(input("Quanto por hora o funcionário vai receber: "))
        else:
            self.per_hour = per_hour_prev
        self.money = 0
        self.name_type = "Horista"
        self.payment_agenda = "semanalmente"
        self.print_data()

        @property
        def per_hour(self):
            return self._per_hour
        
        @property
        def money(self):
            return self._money

        @property
        def name_type(self):
            return self._name_type

        @property
        def payment_agenda(self):
            return self._payment_agenda

        @per_hour.setter
        def per_hour(self, value):
            self._per_hour = value

        @money.setter
        def money(self, value):
            self._money = value

        @name_type.setter
        def name_type(self, value):
            self._name_type = value

        @payment_agenda.setter
        def payment_agenda(self, value):
            self._payment_agenda = value

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

class Month(Employee):
    
    def __init__(self, name, address,type_of_payment, syndicate, Id, salary_prev=0):
        try:
            super().__init__(name, address,type_of_payment, syndicate, Id, syndicate.Id, syndicate.syndicate_fee, syndicate.total_fee)
        except:
            super().__init__(name, address,type_of_payment, syndicate, Id)
        if not salary_prev:
            self.salary = int(input("Quanto vai ser o salário do funcionário: "))
        else:
            self.salary = salary_prev
        self.money = self.salary
        self.name_type = "Mensal"
        self.payment_agenda = "mensalmente"
        self.print_data()

        @property
        def salary(self):
            return self._salary

        @property
        def money(self):
            return self._money

        @property
        def name_type(self):
            return self._name_type

        @property
        def payment_agenda(self):
            return self._payment_agenda

        @salary.setter
        def salary(self, value):
            self._salary = value

        @money.setter
        def money(self, value):
            self._money = value

        @name_type.setter
        def name_type(self, value):
            self._name_type = value

        @payment_agenda.setter
        def payment_agenda(self, value):
            self._payment_agenda = value

    def paid(self):
        value = self.money
        return value

class Comission(Month):
    
    def __init__(self, name, address,type_of_payment, syndicate, Id, salary_prev=0, comission_percent_prev=0):
        if not comission_percent_prev:
            self.comission_percent = int(input("Quanto vai ser a comissão do funcionário: "))/100
        else:
            self.comission_percent = comission_percent_prev
        try:
            super().__init__(name, address,type_of_payment, syndicate, Id, salary_prev, syndicate.Id, syndicate.syndicate_fee, syndicate.total_fee)
        except:
            super().__init__(name, address,type_of_payment, syndicate, Id, salary_prev)
        self.name_type = "Comissionado"
        self.payment_agenda = "bi-semanalmente"

    @property
    def comission_percent(self):
        return self._comission_percent

    @comission_percent.setter
    def comission_percent(self, value):
        self._comission_percent = value

    def sell_results(self, value):
        self.money += (self.comission_percent*value)

    def paid(self):
        value = self.money
        self.money = self.salary
        return value
