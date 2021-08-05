from format import confirm_changes, load_changes
from interface import start

employees = []

while True:
    start(employees)
    confirm_changes(employees)
    try:
        employees = load_changes()
    except:
        pass
6