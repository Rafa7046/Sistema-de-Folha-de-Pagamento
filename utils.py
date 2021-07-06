import random
from payments import Comission, Hourly, Month


def check_type_of_worker_payment(type_of_worker):
    if type_of_worker.lower() == "hourly" or type_of_worker.lower() == "hour" or type_of_worker.lower() == "hora":
        return Hourly()
    elif type_of_worker.lower() == "month" or type_of_worker.lower() == "monthly" or type_of_worker.lower() == "mensal":
        return Month()
    elif type_of_worker.lower() == "comission" or type_of_worker.lower() == "comissao":
        return Comission()

def find_worker(reference, employees):
    return next((employee for employee in employees if employee.Id == reference), None )

def generate_id():
    Id_list = []
    Id = random.randint(1, 10000)
    while Id in Id_list:
        Id = random.randint(1, 10000)
    Id_list.append(Id)
    return Id