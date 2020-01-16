import datetime
from application.salary import calculate_salary
from application.db.get_employees import get_employees

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(datetime.datetime.now().strftime("%Y%m%d"))