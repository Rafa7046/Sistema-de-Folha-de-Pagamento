import dill
from employee import employees

employee_json = {}

# def format_employee():
#     for x in employees:
#         employee_json['data'] = []
#         employee_json['data'].append({
#             'name': x.name ,
#             'address': x.address ,
#             'type_of_worker': x.type_of_worker ,
#             'type_of_payment': x.type_of_payment ,
#             'syndicate': x.syndicate ,
#             'Id': x.Id ,
#         })

def save_object():
    with open('data.pkl', 'wb') as output:
        dill.dump(employees, output, dill.HIGHEST_PROTOCOL)
