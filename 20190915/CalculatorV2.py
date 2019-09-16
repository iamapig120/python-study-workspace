# 使用栈实现的计算器
def calc(formula: str) -> int:
    # 符号定义
    bracket_left_char = '('
    bracket_right_char = ')'
    symbols = ['+', '-', '*', '/', '%', '^']
    priority_level = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '%': 2,
        '^': 3
    }
    # 数字
    num_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # 数字Buf
    number_buffer = ""
    # 括号开始于
    bracket_start = 0
    # 括号包含内容长度
    bracket_count = 0
    # 数字 栈
    numbers_stack = []
    # 运算符 栈
    symbols_stack = []
    # 给定 a,b,符号 计算结果

    def __calc_a_b__(a: int, b: int, symbol: str) -> int:
        print(a, b, symbol)
        if symbol == '+':
            return b + a
        elif symbol == '-':
            return b - a
        elif symbol == '*':
            return b * a
        elif symbol == '/':
            return b // a
        elif symbol == '%':
            return b % a
        elif symbol == '^':
            return b ** a
    # 检查是否存在括号并递归
    # 就这里这个 range ，避免使用
    for index, char in enumerate(formula):
        if char == bracket_left_char:
            bracket_count += 1
            if(bracket_count == 1):
                bracket_start = index
        elif char == bracket_right_char:
            bracket_count -= 1
            if bracket_count == 0:
                # print("括号内容运算" + formula[bracketStart + 1: index])
                numbers_stack.append(calc(formula[bracket_start + 1: index]))
        elif bracket_count == 0:
            # 如果为数字
            if char in num_chars:
                number_buffer += char
            elif char in symbols:
                # 将数字入栈
                if len(number_buffer):
                    numbers_stack.append(int(number_buffer))
                    number_buffer = ''
                # 负号单独处理
                if char == '-':
                    if index == 0 or formula[index - 1] in symbols or formula[index - 1] == bracket_right_char:
                        number_buffer += char
                # 如果符号运算优先级低于栈，则将栈清理到和当前运算级相等为止
                while len(symbols_stack) and symbols_stack[len(symbols_stack)-1]["level"] > priority_level[char]:
                    numbers_stack.append(__calc_a_b__(
                        numbers_stack.pop(), numbers_stack.pop(), symbols_stack.pop()["symbol"]))
                symbols_stack.append({
                    "level": priority_level[char],
                    "symbol": char
                })
    # 递归结束后，按照栈直接进行计算
    # 先检测是否有数字未入栈
    if len(number_buffer):
        numbers_stack.append(int(number_buffer))
    # 进行计算
    while len(symbols_stack):
        numbers_stack.append(__calc_a_b__(
            numbers_stack.pop(), numbers_stack.pop(), symbols_stack.pop()["symbol"]))
    return numbers_stack.pop()


# while True:
#     print("运算结果\n" + str(calc(input("输入算式\n")))+'\n')
