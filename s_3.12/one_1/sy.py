"""
import random
list=[random.randint(1,100) for i in range(20)]
list1=sorted(list[::2],reverse=True)
list[::2]=list1
print(list)
"""

'''
pythonSet = {'王雪','李明','唐德','罗明'}
cSet = {'朱佳','李明','唐德','杨鹏'}
javaSet = {'李思','李明','郑君','罗明'}
pynotc=pythonSet.difference(cSet)
ThreeCan=pythonSet&cSet&javaSet
t1=pythonSet&cSet
t2=pythonSet&javaSet
t3=cSet&javaSet
TwoCan=t1&t2&t3
print(pynotc)
print(ThreeCan)
print(TwoCan)
'''

'''
import random
import string
a=string.ascii_letters+string.digits
password=''.join(random.sample(a,8))
print(password)
'''


import random
import string
from collections import Counter
a=string.ascii_letters+string.digits
list=''.join(random.choices(a,k=1000))
charcount=dict(Counter(list))
for char,count in charcount.items():
    print(char,count)





'''
num=0
i=0
while i<=64 :
    num+=2**i
    i+=1
print(num)
'''

'''
a=input().split()
b,c=map(int,input().split())
list=a[b:c:1]
print(list)
'''


'''
import random
lst_who=['小马','小羊','小鹿']
lst_where=['草地上','电影院','家里']
lst_what=['看电影','听故事','吃晚饭']
num1=int(random.uniform(0,2))
num2=int(random.uniform(0,2))
num3=int(random.uniform(0,2))
list=lst_who[num1]+lst_where[num2]+lst_what[num3]
print(list)
'''

'''
import random
import string
a=string.ascii_letters+string.digits
password=''.join(random.sample(a,20))
list1=password[:10]
list3=sorted(list1)
list2=password[10:]
list4=sorted(list2,reverse=True)
list=list3+list4
print(list)
'''

'''
str=input()
str1=''.join(sorted(str))
print(str1)
print(str1[::-1])
'''



'''
list_a=(1,7,9,11,13,15,17,19)

list_b=(2,4,6,8,10)
c=sorted(list_b+list_a)
c.insert(2,"fanyap")
print(c)

'''
'''
list={'ww','ee','rr','tt','ww','ee'}
lit=set(list)
print(lit)
'''





