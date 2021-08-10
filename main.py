from format import load_changes
from interface import start

employees = []

while True:
    try:
        employees = load_changes("data.pkl")
    except:
        pass
    employees = start(employees)