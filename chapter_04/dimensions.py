dimensions = (200,50)
# print(dimensions[0])
# print(dimensions[1])

# # dimensions[0] = 250 #this produces an error because tuples are immutable (unchageable)

# for dimension in dimensions:
#     print(dimension)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100) #while you can't change a tuple, you can write over it
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)