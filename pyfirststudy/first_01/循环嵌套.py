#外层：表白一百天的控制
# 内层：每天的表白都送10枝玫瑰花
i=1
while i<=100:
    print(f"今天是第{i}天,准备表白。。。。")
    #内层
    j=1
    while j<=10:
        print(f"送给小美的第{j}枝花")
        j+=1
    print("小美，黑马喜欢你！！！")
    i+=1
print(f"坚持到第{i-1}天，表白成功！")
#不换行
#print("hello",end='')
#print("world",end='')

print("hello\tworld")
print("heima\t程序员")