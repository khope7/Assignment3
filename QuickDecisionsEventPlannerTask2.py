#Task 2: Venue Selection Based on the corrected code from Task 1, further enhance your code to recommend additional things like "audio system" or "projector" based on the number of attendees.

#Copying code from QuickDecisionsEventPlannerTask1 with adjusted coding for Task2, specified lower number for audio system and projectors by catching numbers less than 100 with anything beyond defaulting to large hall
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