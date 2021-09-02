"""
Georgia Institute of Technology - CS1301
HW02 - Conditionals
"""

#########################################

"""
Function Name: intramuralGames()
Parameters: gameName (str), numFriends (int)
Returns: None (NoneType)
"""
def intramuralGames(gameName, numFriends):
    
    if numFriends <  8*.25:
        print("Let's choose something else.")
    elif numFriends >= 8*.25 and numFriends < 8*.75:
        print("We will try out {} for a little bit!".format(gameName))
    elif numFriends >= 8*.75:
        print("Let's register for {}!!!".format(gameName))
    


#########################################

"""
Function Name: goShopping()
Parameters: item (str), quantity (int), budget (float)
Returns: moneyLeft (float) or error message (str)
"""
def goShopping(item, quantity, budget):
    if item == "Shorts" and quantity*13<budget:
        return budget -(quantity*13.00)
    elif item == "T-Shirts and Tanks" and quantity*9.75<budget:
        return budget -(quantity*9.75)
    elif item == "Swimwear" and quantity*20.00<budget:
        return budget - (quantity*20.00)
    elif item == "Sunglasses" and quantity*7.50<budget:
        return budget - (quantity*7.50)
    elif item == "Slides" and quantity*15.50<budget:
        return budget - (quantity*15.50)
    else:
        return "Not enough money!"


#########################################

"""
Function Name: getDinner()
Parameters: budget (float), diningOption (str)
Returns: restaurantName (str)
"""
def getDinner(budget, diningOption):
    if budget<=10.00 and (diningOption =="Takeout" or diningOption =="Delivery"):
        return "Chick Fil A"
    elif budget<=10.00 and(diningOption =="Indoor" or diningOption =="Outdoor"):
        return "Moe's"
    elif budget > 10.00 and budget <=20.00 and (diningOption=="Indoor" or diningOption=="Takeout"):
        return "Tin Drum"
    elif budget >10.00 and budget <=20.00 and (diningOption=="Outdoor" or diningOption=="Delivery"):
        return "Umma's"
    elif budget > 20.00 and budget <= 30.00 and (diningOption=="Indoor" or diningOption=="Outdoor" or diningOption=="Takeout"):
        return "Yeah Burger"
    elif budget >20.00 and budget <=30.00 and (diningOption=="Delivery"):
        return "Flip Burger"
    elif budget > 30.00 and budget <= 40.00 and diningOption=="Indoor":
        return "Two Urban Licks"
    elif budget > 30.00 and budget <= 40.00 and (diningOption =="Takeout" or diningOption=="Delivery" or diningOption=="Outdoor"):
        return "Gypsy Kitchen"
    

#########################################

"""
Function Name: backupRestaurant()
Parameters: budget (float), diningOption (str), backup (str)
Returns: decision (str)
"""
def backupRestaurant(prefer_restaurant, backup):
    
    if prefer_restaurant == "Chick Fil A" or prefer_restaurant=="Umma's" or prefer_restaurant=="Gypsy Kitchen" or prefer_restaurant=="Flip Burger":
        return "Yay, you can get dinner at your first choice, {}.".format(prefer_restaurant)
    else:
        return "You'll have to get dinner at {} instead.".format(backup)


#########################################

"""
Function Name: rideShare()
Parameters: number of riders (int), miles(int), rideShareOptionaA (str), rideShareOptionaB (str)
Returns: rideShareOption (str)
"""
def calculatecost(option, riders, miles):
    if option=="Uber" and riders<=3:
        return 5+(5.50*miles)
    elif option=="Uber" and riders>3:
        return 5.50*miles
    elif option=="Taxi":
        return miles*18.00
    elif option=="Lyft":
        return 10+(1.50*miles)
    elif option=="Hitch" and riders>2:
        return (miles*7.50)-(riders*10.00)
    elif option=="Hitch" and riders<=2:
        return miles*7.50


def rideShare(riders, miles, optionA, optionB):
    cost_of_A= calculatecost(optionA, riders, miles)
    cost_of_B=calculatecost(optionB, riders, miles)
    if cost_of_A > cost_of_B:
        return optionB
    elif cost_of_B > cost_of_A:
        return optionA
    elif cost_of_A == cost_of_B:
        return optionA


