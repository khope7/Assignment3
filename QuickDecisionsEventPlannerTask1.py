#Task 1: Code Correction You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

#Buggy Code:
#
#attendees = input("Enter number of attendees: ")
#venue = "large hall" if attendees > 100 else "conference room"
#print(venue)

#Writing corrected code, adjusted to create user input as integer and created conditional statement with correct indentation and formatting
attendees = int(input("Enter number of attendees: "))

if attendees > 100:
    venue = "large hall"
else:
    venue = "conference room"

print(venue)