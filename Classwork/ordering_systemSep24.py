name = input("PLease enter a name for the order: ")
age = input("How old are you?: ")

if not (age > 12):
    print("You are too young to order a slushee.")
else:
    print("Hello " + name + "!")
    cost = int(input("How many slushees would you like?: ")) * 1.99
    if (cost > 4):
        print("Suprise! Today's deal is by 3 or more, get one free!")
        print("Your total is " + str(cost - 1.99))
    else:
        print("Your total is " + str(cost))