from employee import Employee, employees
from interface import start

while True:
    start()
    if input("Deseja realizar outra operação? [sim] [nao]\n") == "nao":
        break

# for workers in employees:
#     workers.print_data()