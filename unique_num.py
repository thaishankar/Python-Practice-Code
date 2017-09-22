dishes = {"Pasta":["Tomato Sauce", "Onions", "Garlic"],
"Chicken Curry":["Chicken", "Curry Sauce"],
"Fried Rice":["Rice", "Onions", "Nuts"],
"Salad":["Spinach", "Nuts"],
"Sandwich":["Cheese", "Bread"],
"Quesadilla":["Chicken", "Cheese"]}

def groupByIngredients(dishes):
    by_ingredients = {}
    for dish in dishes:
        for ingredient in dishes[dish]:
            if ingredient in by_ingredients:
                by_ingredients[ingredient].append(dish) 
            else:
                by_ingredients[ingredient] = [dish]
                
    return by_ingredients
if __name__ == '__main__':
    print groupByIngredients(dishes)
