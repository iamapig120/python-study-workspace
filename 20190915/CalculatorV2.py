# 使用栈实现的计算器

# 计算器错误


class CalcError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)  # 初始化父类
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo


def calc(formula: str, *, portion=False) -> int or str:
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

    # 将字符串转为int
    def buf_to_int(buff: str) -> int or str:
        num_flag = False
        for num_char in num_chars:
            if num_char in buff:
                num_flag = True
                break
        if not num_flag:
            if portion:
                return buff
            else:
                raise CalcError("无效输入")
        return int(buff)

    # 给定 a,b,符号 计算结果

    def __calc_a_b__(a: int or str, b: int or str, symbol: str) -> int:
        print(a, b, symbol)
        a = int(a)
        b = int(b)
        if symbol == '+':
            return b + a
        elif symbol == '-':
            return b - a
        elif symbol == '*':
            return b * a
        elif symbol == '/':
            if a == 0:
                raise CalcError("除数不能为 0")
            return b // a
        elif symbol == '%':
            return b % a
        elif symbol == '^':
            return b ** a
    # 检查是否存在括号并递归
    for index, char in enumerate(formula):
        if char == bracket_left_char:
            bracket_count += 1
            if(bracket_count == 1):
                bracket_start = index
        elif char == bracket_right_char:
            bracket_count -= 1
            if bracket_count == 0:
                # print("括号内容运算" + formula[bracketStart + 1: index])
                numbers_stack.append(
                    calc(formula[bracket_start + 1: index], portion=False))
            elif bracket_count < 0:
                raise CalcError("括号不匹配")
        elif bracket_count == 0:
            # 如果为数字
            if char in num_chars:
                number_buffer += char
            elif char in symbols:
                # 将数字入栈
                if len(number_buffer):
                    numbers_stack.append(buf_to_int(number_buffer))
                    number_buffer = ''
                # 负号单独处理
                if char == '-':
                    if index == 0 or formula[index - 1] in symbols or formula[index - 1] == bracket_left_char:
                        number_buffer += char
                        continue
                # 如果符号运算优先级低于或等于栈，则将栈清理到比当前运算级低为止
                while len(symbols_stack) and symbols_stack[len(symbols_stack)-1]["level"] >= priority_level[char] and len(numbers_stack) > 1:
                    numbers_stack.append(__calc_a_b__(
                        numbers_stack.pop(), numbers_stack.pop(), symbols_stack.pop()["symbol"]))
                symbols_stack.append({
                    "level": priority_level[char],
                    "symbol": char
                })
    # 递归结束后，按照栈直接进行计算
    # 检测括号是否匹配
    if bracket_count:
        if portion:
            numbers_stack.append(
                calc(formula[bracket_start+1:], portion=portion))
        else:
            raise CalcError("括号不匹配")
    # 检测是否有数字未入栈
    elif len(number_buffer):
        numbers_stack.append(buf_to_int(number_buffer))
    # 如果算式为部分算式
    if portion:
        if len(numbers_stack) and len(str(numbers_stack[len(numbers_stack)-1])):
            return str(numbers_stack[len(numbers_stack)-1])
        return 0
    # 进行计算
    while len(symbols_stack) and len(numbers_stack) > 1:
        numbers_stack.append(__calc_a_b__(
            numbers_stack.pop(), numbers_stack.pop(), symbols_stack.pop()["symbol"]))
    if len(numbers_stack) > 1 or len(symbols_stack) and not portion:
        raise CalcError("无效输入")
    if len(numbers_stack):
        return numbers_stack.pop()
    else:
        return 0


# while True:
#     print("运算结果\n" + str(calc(input("输入算式\n")))+'\n')
