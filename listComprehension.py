names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
#Accepts items with the small letter “o” in the new list
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)
#Accepts items which have more than 4 letters
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)