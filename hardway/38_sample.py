ten_things = "Apples Oranges Banana Telephone Crow Tele Car"

print ('-' * 15)
print ("Wait there isn't enough ten things")

stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Summer","Spring","Rain","Mobile"] 

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print ("Adding ", next_one)
	stuff.append(next_one)
	print("There are %d items in stuff " % len(stuff))

print ("Stuffs ::", stuff)
print ("join ", (" ").join(stuff) )












