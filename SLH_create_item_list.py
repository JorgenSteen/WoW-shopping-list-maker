


from pprint import pprint
from SLH_full_wow_item_list import full_item_list
#from SLH_craftable_ingredient_list import craft_recipes

output_dict_item_list = {}
output_dict_item_class = ""

for item_id, name in full_item_list.items():
    output_dict_item_list[item_id] = {"name":name.encode("ASCII", errors="ignore").decode("ASCII"), "effect":"No effect", "price": -1}


# Creates this format {"ITEM_ID": {"name": "name of item", "effect": "effect of item", "price": item_price},
with open("SLH_item_info.py", "w") as f:
    f.write("item_info = {\n")
    for item_id, info in output_dict_item_list.items():
        f.write(f"    {item_id}:{info},\n")
    f.write("}\n")

# Creates this format
#class Consumable:
#    GreateNatureResistancePotion = "Item_ID"
#    MajorManaPotion = "Item_ID"
with open("SLH_item_name.py", "w") as f:
    f.write("class Item:\n")
    for item_id, info in output_dict_item_list.items():
        name = info["name"]
        banned_list = [" ", "-","'",":","[","]","(",")","/",".","!","&","#"]

        for char in banned_list:
            name = name.replace(char,"")
        f.write(f"    {name} = {item_id}\n")
    f.write("\n")