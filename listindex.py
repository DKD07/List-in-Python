colors=["Red","Green","Blue","Yellow","Green"]
#Positive Indexing
print(colors[2])
print(colors[4])
print(colors[0])
#Negative Indexing
print(colors[-1])
print(colors[-3])
print(colors[-5])
#Check whether the item is present in the list or not
if "Yellow" in colors:
    print("Yellow is present")
else:
    print("Yellow is absdent")
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	
print(animals[-7:-2])	
print(animals[4:])	
print(animals[-4:])
print(animals[:6])	
print(animals[:-3])
#Printing every 3rd consecutive value withing a given range
print(animals[1:8:3])