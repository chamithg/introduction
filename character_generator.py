from dice_roller import roll_dice

#generate a new D&D charactes , gygax style.
# third dice rolls down the board for each of six states
#STR, DEX, CON, WIS, INT, CHA


def generate_new_chararcter():
    character = {"STR": None,
    "DEX": None,
    "CON": None,
    "WIS": None,
    "INT": None,
    "CHA": None,} # list of six items, each representing a single staticstic. (dictionary)

    for stat in character.keys(): #<---- character.keys() this will return the length of key value pairs. 
        dice_roll = roll_dice(6,3)
        character[stat] = dice_roll


    return character

print(generate_new_chararcter())