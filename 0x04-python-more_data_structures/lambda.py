sum = lambda x, y: x + y

print("Sum: ", sum(4, 5))

can_vote = lambda age: True if age >= 18 else False

print("Can Vote: ", can_vote(19))

powerList = [lambda x: x ** 2,
             lambda x: x ** 3,
             lambda x: x ** 4]

for func in powerList:
    print(func(2))
