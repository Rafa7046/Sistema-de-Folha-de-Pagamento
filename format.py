import dill
import os

def save_object(employees, file):
    with open(file, 'wb') as output:
        dill.dump(employees, output, dill.HIGHEST_PROTOCOL)

def load_changes(file): 
    with open(file, 'rb') as input:
        return dill.load(input)


def end_code():
    try:
        os.remove("data.pkl")
    except:
        pass
    try:
        os.remove("data_backup.pkl")
    except:
        pass