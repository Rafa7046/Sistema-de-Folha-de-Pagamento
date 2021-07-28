import dill

def save_object(employees):
    with open('data.pkl', 'wb') as output:
        dill.dump(employees, output, dill.HIGHEST_PROTOCOL)

def confirm_changes(employees):
    if input("Tem certeza dessa alteração? Se quiser desfazer a operação digite 'nao' caso queira manter as alterações digite 'sim' :\n") == "nao":
        if input("Operação foi desfeita, caso queira refazer digite 'refazer' caso contrario digite 'continuar': \n") == "continuar":
            return
        else:
            confirm_changes()
    save_object(employees)
    return

def load_changes(): 
    with open('data.pkl', 'rb') as input:
        return dill.load(input)