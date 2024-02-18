"""
range语句
1：range(num)
  获取一个从0开始，到num结束的但不包含num的数字序列
  eg:range(5)取得的数据是[0,1,2,3,4]

2: range(num1,num2)
   获取一个从num1开始，到num2结束的但不包含num2的数字序列
   eg: range(5,10)取得的数据是[5,6,7,8,9]

3: range(num1,num2,step)
   获取一个从num1开始，到nu2结束的但不包含num的数字序列
   数字之间的步长，以step为准（step默认为1)
   eg: range(5,10,2)取得的数据是：[5,7,9]

"""
# 判断偶数
# 1-100不含100内的偶数
num = int(input("请输入num："))
count = 0
for x in range(1, num):
    if x % 2 == 0:
        count += 1
print(f"共有{count}个偶数")
