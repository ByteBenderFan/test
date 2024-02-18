import random

num = random.randint(1, 10)
guess_num = int(input("输入你要猜测的数字: "))
if guess_num == num:
    print("恭喜，第一次就猜中了！")
else:
    if guess_num > num:
        print("大了")
    else:
        print("小了")
    guess_num = int(input("再次输入你要猜测的数字："))
    if guess_num == num:
        print("恭喜，第二次就猜中了！")
    else:
        if guess_num > num:
            print("大了")
        else:
            print("小了")
        guess_num = int(input("第三次输入你要猜测的数字："))
        if guess_num == num:
            print("恭喜，第三次就猜中了！")
        else:
            print("三次机会用完了，没有猜中！")
            print("真实数字是：", num)

# 案例要求，构建一个随机的数字变量，有限定范围，有三次的机会猜测数字，通过三层嵌套判断实现
# 每次猜不中会提示大了小了,最后一次如果错误就显示这个随机数
# 这个代码需要使用for循环优化