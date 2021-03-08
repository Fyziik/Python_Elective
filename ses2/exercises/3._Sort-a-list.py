#Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’])
a = ['Claus', 'Ib', 'Per', 'Andreas', 'Ida']
print(a)

#Sort this list by using the sorted() build in function.
print(sorted(a))

#Sort the list in reversed order.
print(sorted(a, reverse=True))

#Sort the list on the lenght of the name.
print(sorted(a, key=len))

#Sort the list based on the last letter in the name.
def sort_by_last_index(x):
    return x[-1]

print(sorted(a, key=sort_by_last_index))

#Sort the list with the names where the letter ‘a’ is in the name first.
def sort_by_names_containing_a(x):
    if 'a' in x:
        return x.index('a')
    return False

print(sorted(a, reverse=True, key=sort_by_names_containing_a))