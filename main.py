import pickle
import dill
from format import save_object
from employee import Employee, employees
from interface import start

while True:
    start()
    if input("Deseja realizar outra operação? [sim] [nao]\n") == "nao":
        break

save_object()

def pickled_items():
    """ Unpickle a file of pickled data. """
    with open('data.pkl', "rb") as f:
        while True:
            try:
                yield dill.load(f)
            except EOFError:
                break

print('employees in pickle file:')
for company in pickled_items():
    print('  name: {}, value: {}'.format(company.name, company.Id))
# for workers in employees:
#     workers.print_data()