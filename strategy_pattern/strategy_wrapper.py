from employee import Employee

'''Strategy Pattern '''
# Employee class determines what type of payment algorithm strategy to use depending on how many hours worked
print('\nStrategy Design Pattern\n')

employee = Employee(10)
employee.record_weekly_hours(40)
week_one_wages = employee.calculate_payment()
print(f'Balance after 40 hours regular pay: {employee.account_balance}')
employee.record_weekly_hours(45)
week_two_wages = employee.calculate_payment()
print(f'Balance after adding 45 hours pay: {employee.account_balance}')