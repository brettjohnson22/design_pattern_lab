class Supervisor:

    def __init__(self, name, title, happiness_percent):
        self.name = name
        self.title = title
        self.happiness_percent = happiness_percent
        self.employees = []

    def display_status(self):
        print(
            f'{self.title} {self.name} shows hapiness level of {self.happiness_percent} percent.')
        for employee in self.employees:
            employee.display_status()

    def add_employee(self, employee):
        self.employees.append(employee)
