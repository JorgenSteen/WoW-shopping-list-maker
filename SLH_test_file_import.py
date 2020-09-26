from pprint import pprint
from SLH_full_wow_item_list import full_item_list
from SLH_craftable_ingredient_list import Craft_recipes
from SLH_item_name import Item
import SLH_create_shopping_BOM

#pprint(craft_recipes)
#pprint(full_item_list)

item_1 = Item.MajorManaPotion
item_2 = Item.GreaterNatureProtectionPotion
print(item_1)
print(item_2)
shopping_list = {item_1 : 3, item_2 : 5}
print(shopping_list)

print(SLH_create_shopping_BOM.get_consum_string(shopping_list))
print(SLH_create_shopping_BOM.get_ingredient_string(shopping_list))

from Example_consume_list import example_shopping_list
shopping_list = example_shopping_list
print(SLH_create_shopping_BOM.get_consum_string(shopping_list))
print(SLH_create_shopping_BOM.get_ingredient_string(shopping_list))