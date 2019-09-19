# 因为字符串解析有问题，已废弃

# 所有要进行检查的字符集
numChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

addChar = '+'
subChar = '-'
symbolChars = ['*', '/', '^', '%']
bracketLeftChar = '('
bracketRightChar = ')'

# 对了，遍历不要用 range ，超粪的
# enumerate 我和你讲这个函数超甜
# enumerate(["998","211","985"])
# -> [(0,"998"),(1,"211"),(2,"985")]


def calc(formula: str) -> str:
    print("输入算式" + formula)
    # 将减法转换0减去该数
    formula = formula.replace('-', '+0-')
    if formula.startswith('+'):
        formula = formula[1:]
    # 当前计算中的算式
    calcFormula = ""
    # 下步要计算的算式
    nextFormula = ""
    # 是否需要计算下步
    nextFormulaCountFlag = True
    # 括号开始于
    bracketStart = 0
    # 括号包含内容长度
    bracketCount = 0
    # 检查是否存在括号并递归
    # 就这里这个 range ，避免使用
    for index in range(len(formula)):
        if formula[index] == bracketLeftChar:
            bracketCount += 1
            if(bracketCount == 1):
                bracketStart = index
        elif formula[index] == bracketRightChar:
            bracketCount -= 1
            if bracketCount == 0:
                # print("括号内容运算" + formula[bracketStart + 1: index])
                childResult = calc(formula[bracketStart + 1: index])
                calcFormula += childResult
                # print("括号检查完毕" + calcFormula)
        elif bracketCount == 0:
            calcFormula += formula[index]
    # 递归结束后，这里应该不再有括号存在，可以直接进行计算
    # 将减法转换0减去该数
    formula = formula.replace('-', '+0-')
    if formula.startswith('+'):
        formula = formula[1:]
    nextFormula = calcFormula
    print("将要计算", nextFormula)
    # 乘除幂 检查，一次循环只能去掉一个符号
    while nextFormulaCountFlag:
        nextFormulaCountFlag = False
        # 开始计算算式
        calcFormula = nextFormula
        nextFormula = ""
        print("要计算的表达式", calcFormula)
        # 还有这里这个 range ，太粪
        for index in range(len(calcFormula)):
            for symbol in symbolChars:
                if calcFormula[index] == symbol:
                    # 如果在算式中找到 乘除幂 符号，则开始查找数字
                    print("找到符号" + symbol)
                    leftNumStr = ""
                    rightNumStr = ""
                    leftCharIndex = index-1
                    rightCharIndex = index+1
                    resultStr = 0
                    # 向左搜索值
                    while leftCharIndex > -1 and calcFormula[leftCharIndex] in numChars:
                        leftNumStr = calcFormula[leftCharIndex] + leftNumStr
                        leftCharIndex -= 1
                    # 向右搜索值
                    while rightCharIndex < len(calcFormula) and calcFormula[rightCharIndex] in numChars:
                        rightNumStr += calcFormula[rightCharIndex]
                        rightCharIndex += 1
                    # 按照符号，计算结果
                    if symbol == '*':
                        # print("Find *")
                        resultStr = int(
                            calcFormula[leftCharIndex+1:index]) * int(calcFormula[index+1:rightCharIndex])
                    elif symbol == '/':
                        # print("Find /")
                        resultStr = int(
                            calcFormula[leftCharIndex+1:index]) // int(calcFormula[index+1:rightCharIndex])
                    elif symbol == '^':
                        # print("Find ^")
                        resultStr = int(
                            calcFormula[leftCharIndex+1:index]) ** int(calcFormula[index+1:rightCharIndex])
                    elif symbol == '%':
                        # print("Find %")
                        resultStr = int(
                            calcFormula[leftCharIndex+1:index]) % int(calcFormula[index+1:rightCharIndex])
                    # 返回拼接计算后的表达式
                    nextFormula = calcFormula[:leftCharIndex+1] + \
                        str(resultStr) + calcFormula[rightCharIndex:]
                    # 通知进行下轮运算
                    nextFormulaCountFlag = True
                    print(calcFormula[leftCharIndex+1:index],
                          calcFormula[index+1:rightCharIndex])
                    print(nextFormula, resultStr)
                    break
            # 如果乘除幂运算过了，则跳出
            if nextFormulaCountFlag:
                break
        # 如果乘除幂运算过了，则跳过加法检查直接进行下轮运算
        if nextFormulaCountFlag:
            continue
        # 还有这里这个 range ，也很粪
        for index in range(len(calcFormula)):
            # 加法计算，一次循环只能去掉一个符号
            if calcFormula[index] == addChar or calcFormula[index] == subChar:
                print("Find Symbol", index)
                leftNumStr = ""
                rightNumStr = ""
                leftCharIndex = index-1
                rightCharIndex = index+1
                resultStr = 0
                while leftCharIndex > -1 and calcFormula[leftCharIndex] in numChars:
                    # print("leftCharIndex", leftCharIndex,"calcFormula[leftCharIndex]", calcFormula[leftCharIndex])
                    leftNumStr = calcFormula[leftCharIndex] + leftNumStr
                    leftCharIndex -= 1
                while rightCharIndex < len(calcFormula) and calcFormula[rightCharIndex] in numChars:
                    # print("rightCharIndex", rightCharIndex,"calcFormula[rightCharIndex]", calcFormula[rightCharIndex])
                    rightNumStr += calcFormula[rightCharIndex]
                    rightCharIndex += 1
                print(calcFormula[leftCharIndex+1: index],
                      calcFormula[index+1: rightCharIndex])
                if calcFormula[index] == addChar:
                    resultStr = int(
                        calcFormula[leftCharIndex+1:index]) + int(calcFormula[index+1:rightCharIndex])
                elif calcFormula[index] == subChar:
                    if len(calcFormula[leftCharIndex+1:index]) == 0:
                        break
                    resultStr = int(
                        calcFormula[leftCharIndex+1:index]) - int(calcFormula[index+1:rightCharIndex])
                nextFormula = calcFormula[:leftCharIndex+1] + \
                    str(resultStr) + calcFormula[rightCharIndex:]
                nextFormulaCountFlag = True
                print("下次运算", nextFormula)
                print(calcFormula[leftCharIndex+1:index],
                      calcFormula[index+1:rightCharIndex])
                print(nextFormula, resultStr)
                break
        # 当找不到任何符号时，跳出
        if nextFormulaCountFlag == False:
            break
    print("返回值", calcFormula)
    # 返回值是字符串
    return calcFormula


# 模块化
# while True:
#     print("运算结果\n" + calc(input("输入算式\n"))+'\n')
