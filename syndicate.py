from functools import total_ordering
from utils import generate_syndicate_id

syndicate_ids = []

class Syndicate:
    
    def __init__(self, Id_prev=0, syndicate_fee_prev=0, total_fee_prev=0):
        if not Id_prev:
            self.Id = generate_syndicate_id(syndicate_ids)
        else:
            self._Id = Id_prev
        if not syndicate_fee_prev:
            self.syndicate_fee = int(input("Insira o valor da taxa do sindicato: "))
        else:
            self.syndicate_fee = syndicate_fee_prev
        if not total_fee_prev:
            self.total_fee = 0
        else:
            self.total_fee = total_fee_prev

    @property
    def Id(self):
        return self._Id

    @property
    def syndicate_fee(self):
        return self._syndicate_fee

    @property
    def total_fee(self):
        return self._total_fee

    @Id.setter
    def Id(self, value):
        self._Id = value

    @syndicate_fee.setter
    def syndicate_fee(self, value):
        self._syndicate_fee = value

    @total_fee.setter
    def total_fee(self, value):
        self._total_fee = value

    def service_fee(self, value):
        self.total_fee += value 

    def info_edit(self, reference):
        if reference.lower() == "id":
            self.Id = input("Digite o novo Id do sindicato: ")
        elif reference.lower() == "taxa do sindicato":
            self.syndicate_fee == input("Digite a nova taxa de sindicato do funcionário: ")

    def delete(self):
        del self