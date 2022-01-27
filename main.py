from dependency_injection.di_wrapper import Garage, Motorcycle, Car, Shovel
from facade_pattern.facade_wrapper import PizzaFacade, Oven, Cheese, Dough, Topping, Sauce
from observer_pattern.observer_wrapper import Publisher, Subscriber
from composite_pattern.composite_wrapper import Supervisor, Worker
from strategy_pattern.employee import Employee


''' Depedency Injection Design Pattern '''
print('Depedency Injection Desing Pattern\n')
# Creating Motorcycle and Car objects
motorcycle = Motorcycle('BMW', 'R90/6', 1975)
car = Car('Ford', 'Mustang', 1966)

print('Creating a garage that is dependent on a motorcycle\n')
# (because that is what is being passed into its constructor)
garage_that_is_dependent_on_motorcycle = Garage(motorcycle)

garage_that_is_dependent_on_motorcycle.use_vehicle()

print('\nCreating a garage that is dependent on a car\n')
# (because that is what is being passed into its constructor)
garage_that_is_dependent_on_car = Garage(car)

garage_that_is_dependent_on_car.use_vehicle()


print('\nPassing an improper dependency to a Garage object\n')
shovel = Shovel()

another_garage = Garage(shovel)

another_garage.use_vehicle()

''' Facade Design Pattern '''

# NOT using the facade design pattern
# - Requires a lot of code to make a pizza
# - Everytime we make a different pizza, we have to write all this code

dough = Dough()
sauce = Sauce('Tomato')
topping = Topping('Green Peppers')
cheese = Cheese('Mozzarella')
oven = Oven()

dough.add_sauce(sauce)
dough.add_cheese(cheese)
dough.add_topping(topping)
oven.set_temperature(425)
oven.set_timer(20)
oven.cook(dough)

# USING the facade desing pattern ***
# - Only need to write two lines of code for each new pizza!

pizza_facade = PizzaFacade('Tomato', 'Green Peppers', 'Mozzarella')
pizza_facade.make_pizza()


''' Obvserver Design Pattern '''
print('\n\nObserver Desing Pattern\n')
publisher = Publisher()

mike = Subscriber('Mike')
nevin = Subscriber('Nevin')
jj = Subscriber('JJ')

publisher.register(mike)
publisher.register(nevin)
publisher.register(jj)

publisher.dispatch('Python Rocks!')
publisher.unregister(nevin)
publisher.dispatch('Keep working on your design patterns!')


''' Composite Design Pattern '''
print('\nComposite Desing Pattern\n')

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


'''Strategy Pattern '''
# Employee class determines what type of payment algorithm strategy to use depending on how many hours worked

employee = Employee(10)
employee.record_weekly_hours(40)
week_one_wages = employee.calculate_payment()
employee.record_weekly_hours(45)
week_two_wages = employee.calculate_payment()