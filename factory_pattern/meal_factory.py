from factory_pattern.pizza import Pizza
from factory_pattern.sushi import Sushi


class MealFactory:
    def create_meal(self, type):
        if type == 'italian':
            return Pizza()
        elif type == 'japanese':
            return Sushi()
