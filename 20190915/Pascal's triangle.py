isInvertedOrder = False


def lineGenerator():  # 这个函数是一个生成器，方法来源于 https://zh.wikipedia.org/wiki/杨辉三角形
    # 定义第一行
    line = [1]
    while True:
        # yield 一行内容
        yield line
        # zip 可以将两个 list 合并为一个包含元组的 list
        # 元组为一对值，包含原有两个 list 各自对应索引的值
        # 如 list([1,2,3],[4,5,6]) -> [(1,4),(2,5),(3,6)]
        line = [L+R for L, R in list(zip([0]+line, line+[0]))]


# 用来保存已经得出的行
linesSet = []
# 输入行数
length = int(input("Enter the number of rows for the Pascal’s triangle: "))
# 记录最大单数位数
maxNumLength = 0
# 记录完整一行的最大宽度
maxLineLength: int
# 一个生成器实例
lineGeneratorObject = lineGenerator()

for i in range(length):
    # 使用 next 方法来迭代
    linesSet.append(next(lineGeneratorObject))

# 取所有行中最大值
temp = linesSet[length-1][length//2]
# 计算位数
while temp:
    temp //= 10
    maxNumLength += 1
# 数字间间隔 2 字符
maxNumLength += 2
# 计算最大行长度
maxLineLength = (maxNumLength) * length

print("******Pascal’s Triangle******")
for index in range(len(linesSet)):
    line = linesSet[len(linesSet) - 1 -
                    index] if isInvertedOrder else linesSet[index]
    lineToPrint = ''
    for number in line:
        # 拼接整行，单个数字居中对齐
        lineToPrint += format(str(number), '^'+str(maxNumLength))
    # 拼接完成，整行居中格式化并输出
    print(format(lineToPrint, '^'+str(maxLineLength)))
