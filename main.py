from employee import Employee, employees
from interface import begining

while True:
    begining()
    if input("") == "Sim":
        break

for worker in employees:
    worker.print_data()