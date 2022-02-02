from meal_factory import MealFactory

'''Factory Pattern'''
# Factory's create_meal method will return an object instance based on string passed in
print('\nFactory Design Pattern\n')

factory = MealFactory()

meal_one = factory.create_meal('lasagna')

print(meal_one.type)

meal_two = factory.create_meal('sushi')

print(meal_two.type)