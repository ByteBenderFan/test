# 前面while代码的改进
# i=1
# for i in range(1,101):
#     print(f"今天是向小美表白的第{i}天")
#     for j in range(1,11):
#         print(f"送给小美的第{j}朵玫瑰花")
#     print(f"小美，我喜欢你(第{i}天的表白结束)")
# print(f"第{i}天，表白成功！！！")


# 九九乘法表改进
#i = 1
for i in range(1, 10):
    #j = 1
    for j in range(1, i + 1):
        print(f"{j}*{i}={j * i}\t", end='')
        #j += 1
    #i += 1
    print()
