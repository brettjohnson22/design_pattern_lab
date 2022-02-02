from lasagna import Lasagna
from sushi import Sushi


class MealFactory:
    def create_meal(self, type):
        if type == 'lasagna':
            return Lasagna()
        elif type == 'sushi':
            return Sushi()
