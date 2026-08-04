#=======================================================
#                 Find Your Dream Vehicle
#=======================================================
print("=======================================================")
print("            Find Your Dream Vehicle")
print("=======================================================")
print()
print("Welcome to Vehicle Pick! I am your helper, Pixal. We will pick from Bike or Car, then pick from the 2 options in those")
print()
print("               1 : Bike")
print("               2 : Car ")
Vehicle= int(input("First pick 1 or 2: "))
if Vehicle == 1: 
    print("You have chosen Bike! Now we will choose from....... ")
    print("    Options : Road bike or Moutain bike ")
    print("            1 : Road Bike ")
    print("           2: Mountain Bike")
    Bike = int(input("Now pick 1 or 2 again!: "))
    if Bike == 1:
        print("  You have chosen Road bike. Now we will see its features")
        print("      Your pick : Road bike ")
        print("Best for : City roads and normal roads ")
        print("  Seats : Nothing special only 1 ")
    elif Bike == 2 : 
        print("  You have chosen mountain bike. Now we will see its features")
        print("      Your pick : Mountain Bike")
        print(" Best for : Mountains and rough terrains")
        print("Seats : normal amount 1")
    else:
        print("UNVALID ANSWER, PLEASE TRY AGAIN.")
elif Vehicle == 2: 
    print("You have chosen Car! Now we will choose from....... ")
    print("    Options : Electric Tesla or Hybrid Lexus ")
    print("            1 : Electric Tesla Model 5 ")
    print("            2 : Hybrid Lexus RX L ")
    Car = int(input("Now pick 1 or 2 again!: "))
    if Car == 1:
        print("  You have chosen Electric Tesla. Now we will see its features")
        print("      Your pick : Electric Tesla ")
        print("Best for : Industry leading Features and High tech cabins and rain proof ")
        print("  Seats : 5 ")
    elif Car == 2 : 
        print("  You have chosen Hybrid Lexus . Now we will see its features")
        print("      Your pick : Hybrid Lexus ")
        print(" Best for : High tech and quiet smooth ride")
        print("Seats : 7")
    else:
        print("UNVALID ANSWER, PLEASE TRY AGAIN.")
else:
    print("UNVALID ANSWER, PLEASE TRY AGAIN.")



print("==================================================================================")
PRINT(" Finished!")