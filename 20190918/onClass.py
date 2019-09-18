import functool

# map

ls = [1, 2, 3, 4]
result = list(map(lambda x: x**2, ls))
result2 = [x**2 for x in ls]

print(result)
print(result2)


def showArguments(*args):
    print(args)
    return args[0] + args[1]


result3 = functools.reduce(showArguments, ls, -10)
result4 = functools.reduce(showArguments, ls)

print(result3)
print(result4)
