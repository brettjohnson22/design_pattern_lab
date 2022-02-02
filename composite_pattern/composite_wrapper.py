from supervisor import Supervisor
from worker import Worker


''' Composite Design Pattern '''
print('\nComposite Design Pattern\n')

matt = Worker('Matt', 'Worker', 80)
angela = Supervisor('Angela', 'CFO', 90)
mike = Supervisor('Mike', 'CEO', 100)
tory = Supervisor('Tory', 'Head of Marketing', 90)
steve = Worker('Steve', 'Worker', 85)

angela.add_employee(matt)
mike.add_employee(angela)
mike.add_employee(tory)
tory.add_employee(steve)

mike.display_status()
