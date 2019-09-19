# 查找子字串位置
def cntSubStrMatchRecursive(target: str, key: str) -> list:
    print(target, key, target[-len(key):] == key)
    return [] if len(target) < len(key) else [*cntSubStrMatchRecursive(target[:-1], key), *[len(target) - len(key)]] if target[-len(key):] == key else [*cntSubStrMatchRecursive(target[:-1], key)]


print(cntSubStrMatchRecursive("absabsab", "bs"))
