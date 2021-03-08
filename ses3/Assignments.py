directors = {'Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'}
management = {'Tine', 'Trunte', 'Rane'}
employees = {'Niels', 'Anna', 'Tine', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'}

#who in the board of directors is not an employee?
print("Director & not Employee: ")
for element in directors:
    if element not in employees:
        print(element)

print("--------------------------")

#who in the board of directors is also an employee?
print("Director & Employee: ")
for element in directors:
    if element in employees:
        print(element)

print("--------------------------")

#how many of the management is also member of the board?
print("# of people who are management & member of board:")
amount = 0
for element in management:
    if element in directors:
        amount += 1

print("Amount: " + str(amount))

print("--------------------------")

#All members of the managent also an employee
print("Management & Employee:")
for element in management:
    if element in employees:
        print(element)

print("--------------------------")

#All members of the management also in the board?
print("Management & board member:")
for element in management:
    if element in directors:
        print(element)

print("--------------------------")

#Who is an employee, member of the management, and a member of the board?
print("Employee, management & board member:")
for element in directors:
    if element in management and element in employees:
            print(element)

print("--------------------------")

#Who of the employee is neither a memeber or the board or management?
print("Employee who is neither board member nor management:")
for element in employees:
    if element not in directors and element not in management:
        print(element)

print("--------------------------")


# Using a list comprehension create a list of tuples from the following datastructure
# {‘a’: ‘Alpha’, ‘b’ : ‘Beta’, ‘g’: ‘Gamma’}
dataStructure = {'a': 'Alpha', 'b' : 'Beta', 'g': 'Gamma'}
newDataStructure = [{(x + " " + dataStructure.get(x))} for x in dataStructure]
print(newDataStructure)

print("--------------------------")

# From these 2 sets:

firstSet = {'a', 'e', 'i', 'o', 'u', 'y'}
secondSet = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

# Perform union, symmetric difference, difference, disjoint
# Union
unionSet = firstSet.union(secondSet)
print("Union set: " + str(unionSet))

# Symmetric difference
symmDifferenceSet = firstSet.symmetric_difference(secondSet)
print("Symmetric difference set: " + str(symmDifferenceSet))

# Difference from 1st list perspective
differenceSet = firstSet.difference(secondSet)
print("Difference set 1st: " + str(differenceSet))

# Difference from 2nd list perspective
differenceSet = secondSet.difference(firstSet)
print("Difference set 2nd: " + str(differenceSet))

# Disjoint
disjoint = firstSet.isdisjoint(secondSet)
print("Disjoint set: " + str(disjoint))

print("--------------------------")

# DATE DECODER
print("Date conversion")
dateNameToNumber = {
    "JAN": 1,
    "FEB": 2,
    "MAR": 3,
    "APR": 4,
    "MAY": 5,
    "JUN": 6,
    "JUL": 7,
    "AUG": 8,
    "SEP": 9,
    "OCT": 10,
    "NOV": 11,
    "DEC": 12
}

def dateStringConverter(date):
    indexOfFirst = date.find("-")
    day = date[:indexOfFirst]
    month = date[indexOfFirst + 1 : indexOfFirst + 4]
    year = date[-2:]

    if int(year) > 21:
        year = "19" + year
    else:
        year = "20" + year
    
    return (
        year,
        dateNameToNumber.get(month),
        day
    )

print(dateStringConverter("8-MAR-85"))
print(dateStringConverter("20-JUL-15"))
print(dateStringConverter("17-NOV-95"))