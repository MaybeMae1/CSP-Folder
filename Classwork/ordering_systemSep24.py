def order_slushee(username):
    print("Hello " + username + "!")
    cost = int(input("How many slushees would you like?: ")) * 1.99
    if (cost > 4):
        print("Suprise! Today's deal is by 3 or more, get one free!")
        print("Your total is $%.2f" % (cost - 1.99))
    else:
        print("Your total is $%.2f" % cost)

name = input("Please enter a name for the order: ")
age = input("How old are you?: ")
ordering = True

if age.isnumeric() == False:
    print("Please enter a number.")
    age = int(input("How old are you?: "))

if age < 0:
    print("You cannot be negative years old.")
    age = int(input("How old are you?: "))

if not (age > 12):
    print("You are too young to order a slushee.")
else:
    while ordering:
        order_slushee(name)
        again = input("Would you like to order again? (yes/no): ")
        if again != "yes" and again != "Yes" and again != "y" and again != "Y" and again != "YES":
            ordering = False
            print("Thank you for your order!")
        