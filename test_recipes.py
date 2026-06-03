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
    assert x.ingredients == [Ingredient("Мука", 500, "г")]

def test_recipe_add_ingredient_2():
    x = Recipe("Хлеб")
    x.add_ingredient(Ingredient("Мука", 500, "г"))
    x.add_ingredient(Ingredient("Мука", 500, "г"))
    assert x.ingredients == [Ingredient("Мука", 1000, "г")]

def test_recipe_scale_1():
    x = Recipe("Хлеб")
    x.add_ingredient(Ingredient("Мука", 500, "г"))
    assert x.scale(2) != x

def test_recipe_scale_2():
    x = Recipe("Хлеб")
    x.add_ingredient(Ingredient("Мука", 500, "г"))
    x.add_ingredient(Ingredient("Вода", 1000, "г"))
    assert x.scale(2).ingredients == [Ingredient("Мука", 1000, "г"), Ingredient("Вода", 2000, "г")]

def test_scale_3():
    x = Recipe("Хлеб")
    with pytest.raises(ValueError):
        x.scale(-1)