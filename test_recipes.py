import pytest
from Ingredient import *
from Recipe import *
from ShoppingList import *

def test_ingredient():
    x = Ingredient("Мука", 500, "г")
    assert x.name == "Мука" and x.quantity == 500.0 and x.unit == "г"

def test_ingredient_str():
    assert str(Ingredient("Мука", 500, "г")) == "Мука: 500.0 г"

def test_ingredient_eq_1():
    assert Ingredient("Мука", 500, "г") == Ingredient("Мука", 100, "г")

def test_ingredient_eq_2():
    assert Ingredient("Мука", 500, "г") != Ingredient("Лук", 500, "г")

def test_ingredient_eq_3():
    assert Ingredient("Мука", 500, "г") != Ingredient("Мука", 500, "кг")

def test_recipe():
    x = Recipe("Хлеб")
    assert x.title == "Хлеб" and x.ingredients == []

def test_recipe_add_ingredient_1():
    x = Recipe("Хлеб")
    x.add_ingredient(Ingredient("Мука", 500, "г"))
    assert x.ingredients == [Ingredient("Мука", 500, "г")] and x.ingredients[0].quantity == 500

def test_recipe_add_ingredient_2():
    x = Recipe("Хлеб")
    x.add_ingredient(Ingredient("Мука", 500, "г"))
    x.add_ingredient(Ingredient("Мука", 500, "г"))
    assert x.ingredients == [Ingredient("Мука", 1000, "г")] and x.ingredients[0].quantity == 1000

def test_recipe_scale_1():
    x = Recipe("Хлеб")
    x.add_ingredient(Ingredient("Мука", 500, "г"))
    assert x.scale(2) != x

def test_recipe_scale_2():
    x = Recipe("Хлеб")
    x.add_ingredient(Ingredient("Мука", 500, "г"))
    x.add_ingredient(Ingredient("Вода", 1000, "г"))
    assert (x.scale(2).ingredients == [Ingredient("Мука", 1000, "г"), Ingredient("Вода", 2000, "г")]
            and x.scale(2).ingredients[0].quantity == 1000) and x.scale(2).ingredients[1].quantity == 2000

def test_scale_3():
    x = Recipe("Хлеб")
    with pytest.raises(ValueError):
        x.scale(-1)

def test_recipe_len():
    x = Recipe("Хлеб")
    x.add_ingredient(Ingredient("Мука", 500, "г"))
    x.add_ingredient(Ingredient("Вода", 1000, "г"))
    x.add_ingredient(Ingredient("Мука", 1000, "г"))
    assert len(x) == 2

def test_shopping_list_add_recipe_1():
    x = Recipe("Хлеб")
    x.add_ingredient(Ingredient("Мука", 500, "г"))
    sl = ShoppingList()
    sl.add_recipe(x, 2)
    assert sl.get_list() == [Ingredient("Мука", 1000, "г")] and sl.get_list()[0].quantity == 1000

def test_shopping_list_add_recipe_2():
    sl = ShoppingList()
    x = Recipe("Хлеб")
    x.add_ingredient(Ingredient("Мука", 500, "г"))
    with pytest.raises(ValueError):
        sl.add_recipe(x, 0)

def test_shopping_list_remove_recipe_1():
    x = Recipe("Хлеб")
    x.add_ingredient(Ingredient("Мука", 500, "г"))
    x.add_ingredient(Ingredient("Вода", 1000, "г"))
    sl = ShoppingList()
    sl.add_recipe(x, 2)
    sl.remove_recipe("Хлеб")
    assert sl.get_list() == []

def test_shopping_list_remove_recipe_2():
    x = Recipe("Хлеб")
    x.add_ingredient(Ingredient("Мука", 500, "г"))
    sl = ShoppingList()
    sl.add_recipe(x, 2)
    sl.remove_recipe("Пиво")
    assert sl.get_list() == [Ingredient("Мука", 1000, "г")] and sl.get_list()[0].quantity == 1000

def test_shopping_list_get_list_1():
    x1 = Recipe("Хлеб")
    x1.add_ingredient(Ingredient("Мука", 500, "г"))
    x2 = Recipe("Пиво")
    x2.add_ingredient(Ingredient("Мука", 1000, "г"))
    sl = ShoppingList()
    sl.add_recipe(x1, 1)
    sl.add_recipe(x2, 1)
    sl_list = sl.get_list()
    assert len(sl_list) == 1 and sl_list[0].quantity == 1500

def test_shopping_list_get_list_2():
    x1 = Recipe("Хлеб")
    x1.add_ingredient(Ingredient("Мука", 500, "г"))
    x2 = Recipe("Пиво")
    x2.add_ingredient(Ingredient("Вода", 1000, "г"))
    sl = ShoppingList()
    sl.add_recipe(x1, 1)
    sl.add_recipe(x2, 1)
    sl_list = sl.get_list()
    assert sl_list[0].name == "Вода" and sl_list[1].name == "Мука"

def test_shopping_list_add_1():
    x1 = Recipe("Хлеб")
    x1.add_ingredient(Ingredient("Мука", 500, "г"))
    x2 = Recipe("Пиво")
    x2.add_ingredient(Ingredient("Вода", 1000, "г"))
    sl1 = ShoppingList()
    sl2 = ShoppingList()
    sl1.add_recipe(x1, 1)
    sl2.add_recipe(x2, 1)
    sl_list = (sl1 + sl2).get_list()
    assert sl_list[0].name == "Вода" and sl_list[1].name == "Мука"

def test_shopping_list_add_2():
    x1 = Recipe("Хлеб")
    x1.add_ingredient(Ingredient("Мука", 500, "г"))
    x2 = Recipe("Пиво")
    x2.add_ingredient(Ingredient("Вода", 1000, "г"))
    sl1 = ShoppingList()
    sl2 = ShoppingList()
    sl1.add_recipe(x1, 1)
    sl2.add_recipe(x2, 1)
    sl3 = sl1 + sl2
    assert len(sl1.get_list()) == 1 and len(sl2.get_list()) == 1 and len(sl3.get_list()) == 2