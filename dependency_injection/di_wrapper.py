from car import Car
from motorcycle import Motorcycle
from garage import Garage
from shovel import Shovel


''' Depedency Injection Design Pattern '''
print('Depedency Injection Design Pattern\n')
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