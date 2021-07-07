from utils import generate_syndicate_id

syndicate_ids = []

class Syndicate:
    
    def __init__(self):
        self.Id = generate_syndicate_id(syndicate_ids)
        self.syndicate_fee = int(input("Insira o valor da taxa do sindicato: "))
        self.total_fee = 0

    def service_fee(self, value):
        self.total_fee += value 


    def info_edit(self, reference):
        if reference.lower() == "id":
            self.Id = input("Digite o novo Id do sindicato: ")
        elif reference.lower() == "taxa do sindicato":
            self.syndicate_fee == input("Digite a nova taxa de sindicato do funcionário: ")


    def delete(self):
        del self