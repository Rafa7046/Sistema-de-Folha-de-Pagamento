import random

def find_worker(reference, employees):
    return next((employee for employee in employees if employee.Id == reference), None )

def generate_id():
    Id_list = []
    Id = random.randint(1, 10000)
    while Id in Id_list:
        Id = random.randint(1, 10000)
    Id_list.append(Id)
    return Id

def generate_syndicate_id(syndicate_Ids):
    Id = random.randint(10000, 20000)
    while Id in syndicate_Ids:
        Id = random.randint(10000, 20000)
    syndicate_Ids.append(Id)
    return Id