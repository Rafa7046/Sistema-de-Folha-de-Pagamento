from format import confirm_changes, load_changes
from interface import start

employees = []

while True:
    start(employees)
    confirm_changes(employees)
    employees = load_changes()
    for worker in employees:
        worker.print_data()
    if input("Deseja realizar outra operação? [sim] [nao]\n") == "nao":
        break
