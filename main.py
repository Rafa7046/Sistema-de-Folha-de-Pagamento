import dill
from format import save_object
from employee import Employee, employees
from interface import start

while True:
    start()
    if input("Deseja realizar outra operação? [sim] [nao]\n") == "nao":
        break

# save_object()

# with open('data.pkl', 'rb') as input:
#     employees = dill.load(input)

# for workers in employees:
#     workers.print_data()