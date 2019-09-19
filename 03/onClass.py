import functools

# map 测试

ls = [1, 2, 3, 4]
result = list(map(lambda x: x**2, ls))
result2 = [x**2 for x in ls]

print(result)
print(result2)

# reduce 测试 
def showArguments(*args):
    # print(args)
    return args[0] + args[1]


result3 = functools.reduce(showArguments, ls, -10) # 带初始值的
result4 = functools.reduce(showArguments, ls)

print(result3)
print(result4)

# fibonacci
def fibonacci_recursion(n: int) -> int:
    return 1 if n == 0 or n == 1 else fibonacci_recursion(n-1) + fibonacci_recursion(n-2)


print(fibonacci_recursion(5))

# 查找子字串位置
def cntSubStrMatchRecursive(target: str, key: str) -> list:
    print(target, key, target[-len(key):] == key)
    return [] if len(target) < len(key) else [*cntSubStrMatchRecursive(target[:-1], key), *[len(target) - len(key)]] if target[-len(key):] == key else [*cntSubStrMatchRecursive(target[:-1], key)]


print(cntSubStrMatchRecursive("absabsab", "bs"))
