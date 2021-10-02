# This program is going to take a string of words
# Then, it will return those words in the opposite order

mywords = 'gorilla, dragon, lion, orc, troll, hippo'

# Then creates the list!

list = mywords.split(",")

# Print in the normal order

print (list)

# And then, print the words backwards!

list.reverse()

print (list)

# And finally, join the words together as they were!

print(''.join(mywords))








