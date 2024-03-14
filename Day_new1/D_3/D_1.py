money = 5000000
name = None
name = input("请输入你的名字：")


def query(show_header):
    if show_header:
        print("---------查询余额---------")
    print(f"{name},您的当前余额为{money}元。")


def saving(num):
    global money
    money += num
    print("---------存款---------")
    print(f"{name},您当前存款{num}元成功")
    query(False)


def moneyChange(num):
    global money
    money = money - num
    print("---------取款---------")
    print(f"{name},您当前取款{num}元成功")
    query(False)


def main():
    print("-------欢迎来到银行系统---------")
    print("请根据提示操作：")
    print("查询余额\t请输入：1")
    print("存款\t请输入：2")
    print("取款\t请输入：3")
    print("退出\t请输入：4")
    return input("请输入您的选择：")


while True:
    keyboard = main()
    if keyboard == "1":
        query(money)
        continue
    elif keyboard == "2":
        num = int(input("您想存入多少钱，请输入："))
        saving(num)
        continue
    elif keyboard == "3":
        num = int(input("您想取出多少钱，请输入："))
        moneyChange(num)
        continue
    else:
        print("程序退出！！！")
        break
#基础版本