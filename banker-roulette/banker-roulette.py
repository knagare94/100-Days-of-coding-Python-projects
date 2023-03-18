import random

names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")
lenght = len(names)
x = lenght - 1
random_meal = random.randint(0, x)
pay = names[random_meal]
print(f"{pay} is going to buy the meal today!")