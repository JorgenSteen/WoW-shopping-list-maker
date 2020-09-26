
#Shoping list form:
# {item_ID : amount, item_ID2 : amount}


from SLH_item_info import item_info
from SLH_craftable_ingredient_list import Craft_recipes
import json

def get_ingredient_list(shopping_list):
    BOM_total = {}
    for item_id, value in shopping_list.items():
        BOM = Craft_recipes[item_id]
        for reagent_ID, reagent_amount in BOM.items():
            current_value = BOM_total.get(reagent_ID, 0)  # Looks for current value of the item
            amount = value * reagent_amount
            BOM_total[reagent_ID] = amount + current_value
    return BOM_total

def _get_item_amount_string(item_list):
    item_string = ""
    for item_id, amount in item_list.items():
        item_name = item_info[item_id]["name"]
        if(amount>0):
            item_string += f"--{amount}x {item_name}\n"
    return item_string


def get_ingredient_string(shopping_list):
    BOM_total = get_ingredient_list(shopping_list)
    ingredients_string = "-Ingredients List- \n"
    ingredients_string += _get_item_amount_string(BOM_total)
    return ingredients_string


def get_consum_string(shopping_list):
    comsum_string = "-Consumable List- \n"
    comsum_string += _get_item_amount_string(shopping_list)
    print(comsum_string)

#rdef get_price():
