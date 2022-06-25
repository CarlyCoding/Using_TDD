
# Error. 1.
# error message requires get_pet_shop_name to be defined. 
# def get_pet_shop_name using dictionary key. 

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
# Use len to give length of list (pets dict key)

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
            return pet






















    






