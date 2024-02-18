a = 9
b = 2
print(a / b)  # 除法
print(a // b)  # 整除
print('"sssdd"')  # 双引号包含单引号
print("'qwer'")  # 双引号包含单引号
# 转义字符\解除引号作用
name_1 = "\"黑马程序员\""
name_2 = '\'黑马程序员\''
print(name_1)
print(name_2)
# 字符串拼接
print("学IT来黑马" + "月薪过万")
name_3 = "绘马程序员"
address = "地址是杀杀杀"
print("我是" + name_3 + address)

# 通过占位的方式完成拼接
name_4 = "黑狗程序员"
message = "学IT来: %s" % name_4
print(message)

class_1 = 57
class_2 = 16781
massade_1 = "python大数据，北京%s期，毕业平均工资为%s" % (class_1, class_2)
print(massade_1)

"""
%s 将内容转换成字符串，放入占位位置
%d 将内容转换成整数，放入占位位置 
%f 将内容转换成浮点型，放入占位位置

"""
# eg:
name_5 = "传智播客"
set_up_year = 2006
stock_price = 19.19
message_3 = "我是：%s,我成立于：%d年，我今天俺的股价是：%f元" % (name_5, set_up_year, stock_price)
print(message_3)
# 字符串格式化——数字精度控制
# 使用辅助符号"m.n"来控制数据的宽度和精度
# m 控制宽度，要求是数字，设置的宽度小于数字本身不生效
# n 控制小数点精度，要求是数字，会进行数字的四舍五入
# 实例
# %5d: 表示将整数的宽度控制在五位，如11被设置为5d,就会变成[空格][空格][空格]11，用三个空格补足宽度
"""
%5.2f:表示将宽度控制为二，将小数点精度控制为二
小数点和小数部分也算入宽度计算。如对11.345设置了%7.2f后，
结果是：[空格][空格]11.35，进行了小数的四舍五入

"""
num_1 = 11
num_2 = 11.345
print("%5d" % num_1)
print("%1d" % num_1)
print("%7.2f" % num_2)
print("%.2f" % num_2)  # 会做四舍五入的
# 快速掌握字符串格式化的方式
# 格式： f"内容{变量}" 快速格式化
print(f"我是{name_5},我成立于：{set_up_year}年,我今天的股票价格是:{stock_price}元")
# 好处是不限数据类型，不做精度控制，输出原样

# 演示对表达式进行格式化
print("1*2的结果是：%d" % (1 * 2))
print(f"1*2的结果是: {1 * 2}")
print("字符串在python中的类型名是:%s" % type("字符串"))
