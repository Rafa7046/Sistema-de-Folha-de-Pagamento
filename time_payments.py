import calendar
import numpy

def find_day(day, month, year):
    date = calendar.weekday(year, month, day)
    return date

def last_day(month, year):
    first_day, last_day = calendar.monthrange(year, month)
    return last_day

def pay_employee(employees, day, month, year):
    for employee in employees:
        type_of_payment = employee.type_of_worker.payment_agenda
        if type_of_payment == "semanalmente" or type_of_payment == "mensalmente" or type_of_payment == "bi-semanalmente":
            if type_of_payment == "semanalmente":
                if find_day(day, month, year) == 4:
                    payment = employee.type_of_worker.money - (employee.syndicate.syndicate_fee + employee.syndicate.total_fee)
                    print(f"O empregado {employee.Id} foi pago R$ {payment}")
            elif type_of_payment == "mensalmente":
                if find_day(day, month, year) == last_day(month, year):
                    payment = employee.type_of_worker.money - (employee.syndicate.syndicate_fee + employee.syndicate.total_fee)
                    print(f"O empregado {employee.Id} foi pago R$ {payment}")
            elif type_of_payment == "bi-semanalmente":
                pass



# def payment_every_week(day, month, year):
#     cal = calendar.monthcalendar(year, month)
#     a = 0
#     x, y = cal.shape
#     first_week = cal[0]
#     second_week = cal[1]
#     third_week = cal[2]
#     forth_week = cal[3]
#     number_of_weeks = 4
#     try:
#         fifith_week = cal[4]
#         number_of_weeks = 5
#     except:
#         pass
#     try:
#         sixth_week = cal[5]
#         number_of_weeks = 6
#     except:
#         pass
#     while a < y:
#         if cal[a][calendar.find_day(day, month, year)]: