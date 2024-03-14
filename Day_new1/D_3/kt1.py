'''a,b=map(int,input().split())
c=a+b
print(c)
'''
'''F=int(input("输入华氏温度："))
if F>= float(-459.67):
    C=5*(F-32)/9
    d=f"{C:.5f}"
print(d)

'''
'''pi=float(3.14159)
r=float(input())
d=2*r
c=pi*r**2
z=2*pi*r
print(f"{d:.4f} {c:.4f} {z:.4f}")
'''
'''pi=float(3.14)
r=int(input())
v=4/3*pi*r**3
print(f"{v:.5f}")
'''
'''
A,B,C=map(int,input().split())
z=A*(0.2)+B*(0.3)+C*(0.5)
print(int(z))
'''
'''
str = input()
if str==str[::-1]:
    print('yes')
else:
    print('no')
'''
'''
ai=input().split()
ai.pop()
for i in range(len(ai)):
    print(int(ai[len(ai) - i - 1]), end=' ')
'''
'''
python
# 读取输入的一串整数
numbers = input().strip().split()  # 将输入按空格分割成整数列表

# 创建一个空列表用于存储整数
integers = []

# 将输入的字符串转换为整数并存入列表
for num in numbers:
    if num == '0':
        break
    integers.append(int(num))

# 倒序输出整数列表
reversed_integers = integers[::-1]

# 输出结果
output = " ".join(map(str, reversed_integers))
print(output)
这段代码首先读取输入的一串整数，并将其分割成整数列表。然后将整数列表倒序排列，
并最终以空格为间隔打印出来，实现了输入一串整数，以0结束，然后倒序输出的功能。'''
'''
num=input().strip().split()
list1=[]
for i in num:
    if i=='0':
        break
    list1.append(int(i))
reversed_list=list1[::-1]
Output=" ".join(map(str,reversed_list))
print(Output)
'''
'''
n=int(input())
list=input().strip().split()
Max=max(list)
print(int(Max))    #print(*input().split(' ')[-2::-1])
'''
'''
n=int(input())
list=input().split()
Max=max(list)
print(int(Max))
'''
'''
n=int(input())
list1=input().split()
list1=[float(x) for x in list1]
ave=sum(list1)/n
print(f"{ave:.4f}")
'''
'''
n=int(input())
sum=0
nums=[]
for i in range(n):
    num=int(input())
    sum+=num
    nums.append(num)
ave=sum/n
print(f"{sum} {ave:.5f}")

'''
'''
k=int(input())
list=input().split()
a=0
b=0
c=0
for i in list:
    if i=='1':
        a+=1
    elif i=='5':
        b+=1
    elif i=='10':
        c+=1
print(f"{a}")
print(f"{b}")
print(f"{c}")
'''
'''
m, n = map(int, input().split())
Sum = 0
for i in range(m, n + 1):
    if i % 2 != 0:
        Sum += i
print(Sum)
'''
'''
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
d=0
if a<60:
    d+=1
if b<60:
    d+=1
if c<60:
    d+=1
if d==1:
    print(1)
else:
    print(0)
    '''
'''
N=int(input())
list={}
for i in range(N):
    score,name=input().split()
    score=int(score)
    list[score]=name
maxdic=max(list.keys())
name=list[maxdic]
print(name)
'''
'''
N=int(input())：从标准输入中读取一个整数，表示学生人数，将其赋值给变量 N。

list={}：创建一个空字典 list，用于存储分数和姓名的键值对。

for i in range(N):：循环 N 次，依次读取每个学生的信息。

score, name=input().split()：从输入中读取一行包含分数和姓名的字符串，使用 split() 方法将其分割成分数和姓名两部分，并分别赋值给 score 和 name。

score=int(score)：将分数转换为整数类型。

list[score]=name：将分数作为键，姓名作为值，存储在字典 list 中。

maxdic=max(list.keys())：使用 max() 函数找到字典 list 中键（即分数）的最大值，将其赋值给 maxdic。

name=list[maxdic]：根据最高分数找到对应的姓名，赋值给变量 name。

print(name)：输出最高分数对应的学生姓名。'''




























