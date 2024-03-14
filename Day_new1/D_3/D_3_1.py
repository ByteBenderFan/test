list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1 = []
list2 = []
list3 = []
for i in list:
    if i % 2 == 0:
        list1.append(i)
    else:
        list2.append(i)
print(list1, list2)
index = 0
while index < len(list):
    a = list[index]
    if a % 2 == 0:
        list3.append(a)
    index += 1
print(list3)

#元组
t1=(1,2,['ithei','mabowen'])

t1[2][1]='lcj'
print(t1)