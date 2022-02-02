from dough import Dough
from sauce import Sauce
from topping import Topping
from cheese import Cheese
from oven import Oven
from pizza_facade import PizzaFacade


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
