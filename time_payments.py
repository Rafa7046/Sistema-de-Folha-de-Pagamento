import calendar
import numpy

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
            type_of_payment = employee.type_of_worker.payment_agenda
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
                    payment = employee.type_of_worker.paid() - sindicate
                    print(f"O empregado {employee.Id} foi pago R$ {payment}")
            elif type_of_payment == "mensalmente":
                if find_day(day, month, year) == last_day(month, year):
                    payment = employee.type_of_worker.paid() - sindicate
                    print(f"O empregado {employee.Id} foi pago R$ {payment}")
            elif type_of_payment == "bi-semanalmente":
                days = two_weeks(int_to_str(find_day(day, month, year)), month, year)
                if day in days:
                    payment = employee.type_of_worker.paid() - sindicate
                    print(f"O empregado {employee.Id} foi pago R$ {payment}")

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