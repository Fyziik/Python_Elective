#Create a list of capital letters in the english alphabet
a = [chr(x) for x in range(65, 91)]
print(a)

#Create a list of capital letter from the english aplhabet, but exclude 4 with the Unicode code point of either 70, 75, 80, 85.
b = [chr(x) for x in range(65, 91) if x not in [70, 75, 80, 85]]
print(b)

#NEED TO LOOK AT
#Create a list of capital letter from from the english aplhabet, but exclude every second between F & O
c = [chr(x) for x in range (65, 91) if x % 2 == 0 ]
print(c)

# Regular List Comprehension
[ (valid item) for (item) in (data structure) ]

# List Comprehension with if statement
[ (valid item) for (item) in (data structure) if (condition) ]

# List comprehension with if else statement
[ (valid item) if (conditon) else (statement) for (item) in (data structure) ]