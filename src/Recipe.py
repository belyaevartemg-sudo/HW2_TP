from Ingredient import *

class Recipe:
    def __init__(self, title, ingredients = None):
        self.title = title
        self.ingredients = ingredients

    def add_ingredient(self, ingredient: Ingredient):
        if ingredient not in self.ingredients:
            self.ingredients.append(ingredient)
        else:
            self.ingredients[self.ingredients.index(ingredient)].quantity += ingredient.quantity

    @staticmethod
    def is_valid_ratio(ratio):
        if type(ratio) == int or type(ratio) == float:
            if ratio > 0:
                return True
            else:
                return False
        else:
            return False

    def scale(self, ratio):
        if Recipe.is_valid_ratio(ratio):
            new_recipe = Recipe(self.title, [])
            for i in self.ingredients:
                new_recipe.ingredients.append(Ingredient(i.name, i.quantity * ratio, i.unit))
            return new_recipe
        else:
            raise ValueError("ratio должно быть положительным числом")

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        text = self.title + ":"
        for i in self.ingredients:
            text += "/n"
            text += " -" + str(i)
        return text