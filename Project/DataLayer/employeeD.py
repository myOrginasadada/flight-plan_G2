import csv
from employee import Employee

class EmployeeData:
    employees = {}
    FILE_NAME = "employees.csv"

    def __init__(self):
        self.load_data_from_file()

    def load_data_from_file(self):
        with open(self.FILE_NAME, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skps the header row
            for row in reader:
                social_security = row[0]
                employee_info = row[1:]
                employee = Employee.from_row(social_security, employee_info)
                self.employees[social_security] = employee

    def save_data_to_file(self):
        with open(self.FILE_NAME, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for employee in self.employees.values():
                writer.writerow(employee.serialize())

    def create_employee(self, employee: Employee):
        self.employees[employee.social_security] = employee
        self.save_data_to_file()

    def get_employee_by_id(self, social_security):
        return self.employees.get(social_security, None)

    def get_employee_list(self):
        return list(self.employees.values())