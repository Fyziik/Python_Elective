a = ['Hello', 'World', 'Huston', 'we', 'are', 'here']

step1 = a[1:-1]
print(step1)

step2 = a[:2]
print(step2)

step3 = a[-2:]
print(step3)

step4 = a[-2:-1]
print(step4)

step5 = a[::2]
print(step5)

step6 = a[::-1]
print(step6)

a = ('Hello', 'World', 'Huston', 'we', 'are', 'here')

step7 = list(a[1:-1])
print(step7)

a = 'Hello World Huston we are here'

step8 = "'" + a[6:-9] + "'"
print(step8)