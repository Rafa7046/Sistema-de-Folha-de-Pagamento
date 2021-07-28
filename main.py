from format import confirm_changes, load_changes
from interface import start

employees = []

while True:
    start(employees)
    confirm_changes(employees)
    employees = load_changes()
    if input("Deseja realizar outra operação? [sim] [nao]\n") == "nao":
        break
