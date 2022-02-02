from factory_pattern.lasagna import Lasagna
from factory_pattern.sushi import Sushi


class MealFactory:
    def create_meal(self, type):
        if type == 'lasagna':
            return Lasagna()
        elif type == 'sushi':
            return Sushi()
