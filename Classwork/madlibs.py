#Ronan Anders
#Mr. Perez
#10/6/26

#Madlibs Project

words = []

def inputs():
    words.append(input("Enter things (plural): "))
    words.append(input("Enter an insect: "))
    words.append(input("Enter a verb: "))
    words.append(input("Enter a phrase: "))
    words.append(input("Enter a color: "))
    words.append(input("Enter an adjective: "))
    words.append(input("Enter a food: "))
    words.append(input("Enter a name: "))
    words.append(input("Enter an adjective: "))
    words.append(input("Enter a place: "))

inputs()
print(f"Last night I dreamed I was a {words[8]} butterfly with {words[4]} splotches that looked like {words[0]}. I flew to {words[9]} with my best friend, {words[7]}, who was a {words[5]} insect. We ate some {words[6]} when we got there and then decided to {words[2]}. The dream ended when I said, '{words[3]}.'")