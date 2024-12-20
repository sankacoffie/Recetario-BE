import json

def consolidate_ingredients(recipes):
    ingredient_totals = {}
    for recipe in recipes:
        ingredients = json.loads(recipe.ingredients)
        for item, qty in ingredients.items():
            if item in ingredient_totals:
                ingredient_totals[item] += qty
            else:
                ingredient_totals[item] = qty
    return ingredient_totals
