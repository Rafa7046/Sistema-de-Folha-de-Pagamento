import calendar

agendas = ["semanalmente", "mensalmente", "bi-semanalmente"]

def convert(lst):
    final_lst = []
    word = ''
    for letter in lst:
        if letter == " ":
            final_lst.append(word)
            word = ''
        else:
            word += letter
    final_lst.append(word)
    return final_lst

def str_to_int(day):
    date = 0
    if day.lower() == "segunda":
        date = 0
    elif day.lower() == "terça" or day.lower() == "terca":
        date = 1
    elif day.lower() == "quarta":
        date = 2
    elif day.lower() == "quinta":
        date = 3
    elif day.lower() == "sexta":
        date = 4
    elif day.lower() == "sabado" or day.lower() == "sábado":
        date = 5
    elif day.lower() == "domingo":
        date = 6
    return  date

def avaliable_agendas():
    a = 0
    for x in agendas:
        print(f"[{a}] :  {x}")
        a += 1
    chosen = int(input())
    return agendas[chosen]

def create_agenda():
    new_agenda = input("Digite a nova agenda: ")
    agendas.append(new_agenda)


def int_to_str(day):
    days_week = [calendar.MONDAY, calendar.TUESDAY, calendar.WEDNESDAY, calendar.THURSDAY, calendar.FRIDAY, calendar.SATURDAY, calendar.SUNDAY]
    return days_week[day]

def find_day(day, month, year):
    date = calendar.weekday(year, month, day)
    return date

def last_day(month, year):
    first_day, last_day = calendar.monthrange(year, month)
    return last_day

def two_weeks(day_to_pay, month, year):

    c = calendar.Calendar(firstweekday=calendar.SUNDAY)
    cal = c.monthdatescalendar(year, month)
    days = []
    second_day = [day for week in cal for day in week if day.weekday() == day_to_pay and day.month == month][1]
    days.append(second_day.day)
    try:
        forth_day = [day for week in cal for day in week if day.weekday() == day_to_pay and day.month == month][3]
    except:
        pass
    days.append(forth_day.day)
    return days

def pay_employee(employees, day, month, year):
    for employee in employees:
        try:
            type_of_payment = employee.payment_agenda
        except:
            pass
        sindicate = 0
        try:
            sindicate = (employee.syndicate.syndicate_fee + employee.syndicate.total_fee)
        except:
            pass
        if type_of_payment == "semanalmente" or type_of_payment == "mensalmente" or type_of_payment == "bi-semanalmente":
            if type_of_payment == "semanalmente":
                if find_day(day, month, year) == 4:
                    payment = employee.paid() - sindicate
                    print(f"O empregado {employee.Id} foi pago R$ {payment}")
            elif type_of_payment == "mensalmente":
                if day == last_day(month, year):
                    payment = employee.paid() - sindicate
                    print(f"O empregado {employee.Id} foi pago R$ {payment}")
            elif type_of_payment == "bi-semanalmente":
                days = two_weeks(4, month, year)
                if day in days:
                    payment = employee.paid() - sindicate
                    print(f"O empregado {employee.Id} foi pago R$ {payment}")
        else:
            lst = convert(str(type_of_payment))
            if len(lst) == 2:
                if lst[1] == "$":
                    if day == last_day(month, year):
                        payment = employee.paid() - sindicate
                        print(f"O empregado {employee.Id} foi pago R$ {payment}")
                else:
                    if day == int(lst[1]):
                        payment = employee.paid() - sindicate
                        print(f"O empregado {employee.Id} foi pago R$ {payment}")
            else:
                if lst[1] == "1":
                    date = str_to_int(lst[2])
                    if find_day(day, month, year) == date:
                        payment = employee.paid() - sindicate
                        print(f"O empregado {employee.Id} foi pago R$ {payment}")
                elif lst[1] == "2":
                    date = str_to_int(lst[2])
                    days = two_weeks(int_to_str(date), month, year)
                    if day in days:
                        payment = employee.paid() - sindicate
                        print(f"O empregado {employee.Id} foi pago R$ {payment}")
