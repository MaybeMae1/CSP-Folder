#Ronan Anderson
#Mr. Perez
#9/1/26

#ATM System

usernames = ["alice", "bob", "charlie", "david"]
pins = ["1234", "5678", "9012", "3456"]#unencrypted passwords!!!!!!
balances = [1000, 500, 750, 2000]
running = True

def username_input():
    username = input("Please enter your username: ")
    if username in usernames:
        return usernames.index(username)
    elif username == "exit":
        print("Exiting the program.")
        return -1
    else:
        print("Username not found. Please try again, or enter 'exit' to quit.")
        return username_input()

def check_pin(user_id, pin):
    if pin == pins[user_id]:
        return True
    else:
        return False

def check_balance(user_id):
    return balances[user_id]

def change_balance(user_id, amount):
    balances[user_id] = balances[user_id] + amount

def choice_input():
    print("What would you like to do?")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    option = int(input("Enter the number of your choice: "))
    if option < 1 or option > 4:
        print("Invalid selection. Please try again")
        option = choice_input()
    return option

def action_handler(choice):
    if choice == 1:
        balance = check_balance(user_id)
        print("Your current balance is: $%.2f" % balance)
    elif choice == 2:
        amount = float(input("Enter the amount to deposit: "))
        change_balance(user_id, amount)
        print("Deposit successful. Your new balance is: $%.2f" % check_balance(user_id))
    elif choice == 3:
        amount= float(input("Enter the amount to withdraw: "))
        if amount > check_balance(user_id):
            print("Insufficient funds.")
        else:
            change_balance(user_id, -1 * amount)
        print("Funds withdrawn. Your new balance is: $%.2f" % check_balance(user_id))


#Main Code

print("|============================|")
print("|  (bank name) ATM System    |")
print("|============================|")

user_id = username_input()
if user_id == -1:
    running = False
input_pin = input("Please enter your PIN: ")
if not check_pin(user_id, input_pin):
    print("Incorrect PIN. Please try again.")

while running:
    action = choice_input()
    if action == 4:  
        print("Exiting the program.")
        running = False
    else:
        action_handler(action)
