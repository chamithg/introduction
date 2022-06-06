from random import randint

#function to roll dice
#roll some number of dice have specific number of sides
#1 number of sides
#return the sum of all dice rolled


def roll_dice(number, sides):    #def roll_dice(number, sides = 6) this makes the sides value to 6 by default if not provided. 
    result = 0
    
    for roll in range(1, number+ 1):
        roll_result = randint(1, sides)
        result = result + roll_result # randint return value both inclusive
        
        


    return result


