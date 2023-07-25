spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    names = list()
    for food in spicy_foods:
        names.append(food["name"])
    return names


def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(
            f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}"
        )


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"].lower() == cuisine.lower():
            return food


def print_spiciest_foods(spicy_foods):
    spiciest_foods = list()
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_foods.append(food)
    print_spicy_foods(spiciest_foods)


def get_average_heat_level(spicy_foods):
    heat_level_total = 0
    counter = 0
    for food in spicy_foods:
        heat_level_total += food["heat_level"]
        counter += 1
    return int(heat_level_total / counter)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
