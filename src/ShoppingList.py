from Ingredient import *
from Recipe import *

class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe: Recipe, portions: float):
        if portions > 0:
            scaled_recipe = recipe.scale(portions)
            for i in scaled_recipe.ingredients:
                self._items.append((i, recipe.title))
        else:
            raise ValueError("Количество порций должно быть положительным")

    def remove_recipe(self, title: str):
        new_items = []
        for i in self._items:
            if i[1] != title:
                new_items.append(i)
        self._items = new_items.copy()

    def get_list(self):
        sl = {}
        for i in self._items:
            key = (i[0].name, i[0].unit)
            if key in sl:
                sl[key] += i[0].quantity
            else:
                sl[key] = i[0].quantity
        result = []
        for key, i in sl.items():
            result.append(Ingredient(key[0], i, key[1]))
        result = sorted(result, key=lambda x: x.name, reverse=False)
        return result

    def __add__(self, other):
        new_items = ShoppingList()
        for i in self._items:
            new_items._items.append(i)
        for i in other._items:
            new_items._items.append(i)
        return new_items