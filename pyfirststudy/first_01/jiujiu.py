# while实现九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={j * i}\t", end='')
        j += 1
    i += 1
    print()
# print空内容，就是输出一个换行
