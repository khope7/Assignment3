#Task 3: Catering Choices Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

#Copying code from QuickDecisionsEventPlannerTask2 with adjusted coding for Task3, created conditional for yes and no with recommendations based on input, all other entries end program
attendees = int(input("Enter number of attendees: "))

if attendees < 10:
    venue = "audio system"
elif attendees < 50:
    venue = "projector"
elif attendees < 100:
    venue = "conference room"
else:
    venue = "large hall"

print(venue)

order = input("Would you like vegetarian food? Please enter yes or no. ")

if order == "yes":
    print('I recommend "Veggie Delight Caterers"')
elif order == "no":
    print('I recommend "Gourmet Meals Caterers"')