#猜数字while配合input
#要求：无限次机会，直到猜中为止，每次猜不中，会提示大了小了，并且提示猜了几次
import random
num=random.randint(1,100)
sum=0
flag=True
while flag:
     gues=int(input("请输入猜测的数字："))
     sum+=1
     if gues==num:
         print("猜中了！")
         flag=f=False#设置False为终止循环的条件
     else:
         if gues>num:
             print("猜测的大了！")
         else:
             print("猜测的小了！")
print(f"您一共猜测了{sum}次")
     