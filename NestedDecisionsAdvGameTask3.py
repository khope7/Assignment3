#Task 3: Default Path If the user makes an invalid choice at any point, incorporate a pass statement to handle it. HINT: How can an else statement be of use here?

#Copying over code from NestedDecisionsAdvGameTask2, adjusting for Task3
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
        
elif place == "cave":
    action2 = input("light a torch or proceed in the dark? ")
    if action2 == "light a torch":
        print("Finally some light!")
    elif action2 == "proceed in the dark":
        print("You stumbled and fell!")
    else:
        pass
else:
    pass