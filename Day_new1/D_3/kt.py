n = int(input("请输入元素的个数:"))
grade = {}

for i in range(n):
    key = input("输入键：")
    value = int(input("输入值："))
    grade[key] = value

max_value = max(grade.values())
max_key = [k for k, v in grade.items() if v == max_value]

print("值最大的jian为:", max_key)
print("值最大的值为:", max_value)