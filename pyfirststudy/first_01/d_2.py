# if elif else
height = int(input("请输入你的身高(cm): "))
vip_level = int(input("请输入你的vip等级(1-5): "))
if height < 120:
    print("身高小于120cm，可以免费。")
elif vip_level > 3:  # 相当于else if
    print("可以免费")
else:
    print("条件都不满足，需要买票10元。")
