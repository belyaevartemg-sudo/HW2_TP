class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients = None):
        self.name = title
        self.ingredients = ingredients