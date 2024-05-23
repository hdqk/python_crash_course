# squares = []
# for value in range(1,11):
#     # square = value ** 2
#     # squares.append(square)

# squares = []
# for value in range(1,11):
#     squares.append(value**2) #more concise way to do the above

squares = [value**2 for value in range(1,11)] #an even more concise way, a list comprehension

print(squares)

digits = list(range(0,10))
print(min(digits)) #smallest value
print(max(digits)) #largest value
print(sum(digits)) #sum of values