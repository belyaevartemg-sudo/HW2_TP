# HW2_TP

## Домашнее задание №2. Объектно-ориентированное программирование. Тестирование. Работа с Git
Программа для управления рецептами блюд, которая позволяет создавать рецепты с ингредиентами, масштабировать порции, поддерживает диетические категории рецептов и создаёт список покупок из нескольких рецептов с суммированием одинаковых ингредиентов

## Как использовать
Импорт классов в вашем коде:
```python
from src.Ingredient import Ingredient
from src.Recipe import Recipe
from src.ShoppingList import ShoppingList
```
Создание рецепта:
```python
x = Recipe("Хлеб")
```
Добавление ингредиента:
```python
x.add_ingredient(Ingredient("Мука", 500, "г"))
```
Масштабирование рецепта на n порций:
```python
x_n = bread.scale(n)
```
Проверка корректности коэффициента масштабирования:
```python
Recipe.is_valid_ratio(2) # True
Recipe.is_valid_ratio(-1) # False
```
Количество уникальных ингредиентов в рецепте:
```python
len(x)
```
Вывод рецепта в виде строки:
```python
print(x)
```
Создание диетического рецепта:
```python
x_veg = DietaryRecipe("Веганский хлеб", "веган")
```
Создание списка покупок из нескольких рецептов:
```python
sl = ShoppingList()
sl.add_recipe(bread, 2) # 2 порции
sl.add_recipe(vegan_bread, 1) # 1 порция
```
Удаление рецепта из списка покупок:
```python
sl.remove_recipe("Хлеб")
```
Получение списка покупок:
```python
items = sl.get_list()
```
Объединение двух списков покупок:
```python
combined = sl1 + sl2
```

## Запуск тестов
```bash
pip install pytest
pytest
```

## Быстрая установка
```bash
git clone https://github.com/belyaevartemg-sudo/HW2_TP.git
cd HW2_TP
pip install -r requirements.txt
pytest
```

## Автор
Беляев Артём ББИ2503
