
# Error. 1.
# error message requires get_pet_shop_name to be defined. 
# def get_pet_shop_name using dictionary key. 

from os import remove


def get_pet_shop_name(shop):
    return shop["name"]

# Error. 2.
# error message requires get_total_cash to be defined.
# def using the two dictionary keys admin & total cash. 

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

# Error. 3. 
# add_or_remove_cash requires definition. 
# Def wants 10 added to admin>total cash eg. cash 
# From failed tests I ascertained it needs 2 arguments & parameters.
# Add 10 to the get_total_cash function- access shop as before. 

def add_or_remove_cash(shop, money):
    shop["admin"]["total_cash"] += money

# Entry 4-
# Initally thought this would be same as prior with -, but func already def so user will calc if -.

# Error 5 
# get_pets_sold requires definition. 
# Use the two dictionary keys admin and pets_sold.

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

# Error 6 
# increase_pets_sold requires definition
# Similar to error 3, increase the get_pets_sold. No return is required as no =

def increase_pets_sold(shop, pets):
    shop["admin"]["pets_sold"] += pets

# Error 7 
# get_stock_count requires definition. 
# The function wants the total of the items in the self.cc_pet_shop list
# Can solve by counting dictionary entries in list as this is == stock (and 6).
# Function should return a result. 
# Use len to give length (number?) of matching pets in dict. 

def get_stock_count(shop):
    return len(shop["pets"])

# Error 8 
# get_pets_by_breed requires definition. 
# Use the perameters shop & breed with if == in a loop. 
# Function should return a result. 

def get_pets_by_breed(shop, breed):
    found_pets = []
    for pet in shop["pets"]:
        if breed == pet["breed"]:
            found_pets.append(pet)
        

    return found_pets

# Error 9 
# find_pet_by_name requires definition. 
# What it wants is if input (name) is equal to dictionary name entry.

def find_pet_by_name(shop, pet_name):
# This line is writing my for loop, and defining pet (I'm adding notes for revision)
    for pet in shop["pets"]:
        if pet_name == pet["name"]:
        # Pet can be returned because it will match input, due to loop & key.
            return pet

# Entry 10 
# This is the same as above, will work now bc of above. 

# Error 11
# remove_pet_by_name requires definition.
# The function wants the input of pet name to remove the matching dictionary entry. 
# Wants a 'value" of none when Arthur is keyed. 
# Run loop to match input to dictonary, and use .remove to remove from dict. 

def remove_pet_by_name(shop, pet_name):
    for pet in shop["pets"]:
        if pet_name == pet["name"]:
            shop["pets"].remove(pet)
            
# Error 12
# add_pet_to_stock requires definition.
# The new pet Bors the Younger should be added into the self.cc_pet_shop stock to take stock to 7 count. 
# Append the dictionary list pets with new_pet. 
def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)

# Error 13 
# get_customer_cash requires definition. 
# Access position 0 is customer list and key cash by using an if function with if 1000. 

























    






