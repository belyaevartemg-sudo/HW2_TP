from Recipe import *
from Ingredient import *

class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients = None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio: float):
        new_recipe = super().scale(ratio)
        return DietaryRecipe(new_recipe.title, self.diet_type, new_recipe.ingredients)

    def __str__(self):
        text = "[" + self.diet_type + "] " + super().__str__()
        return text