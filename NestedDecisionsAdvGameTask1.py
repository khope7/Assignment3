#Task 1: Code Correction You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. Identify and fix them.

#Buggy Code:

#place = input("Choose a place: forest or cave? ")

#if place = "forest":
#    action = input("climb a tree or cross a river?")
#    if action = "climb a tree":
#        print("You found a bird's nest!")
#    else action = "cross a river":
#        print("You found a boat!")
#elif place = "cave":
#    print("You find a hidden treasure!")


#Writing in corrected code
place = input("Choose a place: forest or cave? ")

#adjusted = to ==, added space after river for user friendly input design, changed else to additional nested if elif statement to catch alt user input, all other entries end program
if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")