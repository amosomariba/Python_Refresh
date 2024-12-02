# The del statement removes one or more items from a list.
names = ["John", "Eva", "Laura", "Nick", "Jack"]

# deleting the second item
del names[1]
print(names)

# deleting items from index 1 to index 3
del names[1:4]
print(names)  # Error! List doesn't exist.
