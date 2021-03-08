#Based on this list of tuples: [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]
my_list = [(1,2),(2,2),(3,2),(2,1),(2,2),(1,5), (10,4), (10, 1), (3, 1)]

#Sort the list so the result looks like this: [(2, 1), (3, 1), (10, 1), (1, 2), (2, 2), (2, 2), (3, 2), (10, 4), (1, 5)]

print(sorted(my_list, key=lambda element: (element[1], element[0])))

#This is first sorted by the last element in the tuple and then the first element in the tuple.
#You should do this in 1 step, but it might help you to try it out in 2 steps first.
