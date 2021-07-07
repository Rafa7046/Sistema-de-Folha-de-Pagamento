from utils import generate_syndicate_id

syndicate_ids = []

class Syndicate:
    
    def __init__(self):
        self.Id = generate_syndicate_id(syndicate_ids)
        self.syndicate_fee = int(input("Insira o valor da taxa do sindicato: "))
        self.total_fee = 0

    def service_fee(self, value):
        self.total_fee += value 
