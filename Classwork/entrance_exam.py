name = input("Enter your name: ")
grade = int(input("Enter your grade (0-100): "))

if(grade > 50):
    print("Congratulations " + name + ", you passed the test")
else:
    print("Sorry " + name + ", you need " + str(51 - grade) + " more points to pass.")