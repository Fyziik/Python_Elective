my_list = ['a', 'b', 'c', '1', '2', '3' ]

# List of invalid functions - some dont work because they take multiple arguments and such. And some are straight up for mathematical functionality, 
# which wont work with strings etc.
# abs()
# bin()
# breakpoint()
# bytearray()
# bytes()
# chr()
# compile()
# complex()
# delattr()
# dict()
# divmod()
# eval()
# exec()
# filter()
# float()
# getattr()
# globals()
# hasattr()
# hash()
# hex()
# int()
# isInstance()
# issubclass()
# locals()
# map()
# memoryview()
# next()
# object()
# oct()
# open()
# ord()
# pow()
# range()
# round()
# setattr()
# str()
# sum()
# super()
# vars()
# __import__()



# List of working functions
print(all(my_list))

print(any(my_list))

print(ascii(my_list))

print(bool(my_list))

print(callable(my_list))

print(classmethod(my_list))

#works but takes up too much space in console
#print(dir(my_list))

print(enumerate(my_list))

print(format(my_list))

print(frozenset(my_list))

#help works, but the output takes up too much space in console
#print(help(my_list))

print(id(my_list))

#Works, but have to type input each time so commenting it out for now
#print(input(my_list))

print(iter(my_list))

print(len(my_list))

print(list(my_list))

print(max(my_list))

print(min(my_list))

print(print(my_list))

print(property(my_list))

print(repr(my_list))

print(reversed(my_list))

print(set(my_list))

print(slice(my_list))

print(sorted(my_list))

print(staticmethod(my_list))

print(tuple(my_list))

print(type(my_list))

print(zip(my_list))