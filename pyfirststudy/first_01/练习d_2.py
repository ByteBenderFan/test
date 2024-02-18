# 猜数字
num=5
if int(input("请猜第一个数字: "))==num:
    print("第一次就猜对了！")
elif int(input("猜错了，再猜一次！"))==num:
    print("猜对了！")
elif int(input("猜错了，再来一次吧！"))==num:
    print("猜对了！")
else:
    print("sorry,全猜错了！")
#第三行代码相当于 print("请猜第一个数字: ")
#                if int(input())==num:
#                    print("第一次就猜对了！")
#  