from format import load_changes
from interface import start

employees = []
var = 0

while True:
    if not var:
        try:
            employees = load_changes("data.pkl")
        except:
            pass
    employees, var = start(employees)