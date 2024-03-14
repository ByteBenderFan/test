# list列表
# 1:取出数据
nlist = ["mbw", "lls", "lcj", "wzh", "zhh", "fyp"]
for i in range(6):#正向索引取值
    print(nlist[i], end=',')
    print(i)
print("")
for i in range(6):#反向索引取值
    num = i - 6
    print(nlist[num], end=',')
    print(num)

#嵌套列表
new_list=[[1,2,3],[4,5,6]]
print(new_list[0][1])

#查找某元素的下标索引
#语法  列表.index(元素)
In=new_list.index([1,2,3])
print(f"[1,2,3]元素的下标索引是：{In}")

#修改特定位置的元素值
list_2=['李传杰','大D哥','赵浩瀚好汉',"马博文666","王子涵说唱家"]
print(f"修改前为：{list_2[2]}")
list_2[2]="小黑牛逼PLUS"
print(f"修改后为：{list_2[2]}")
#插入元素
#方法：列表.insert(x,y), x为被插入的元素的索引+1,y为要插入的元素
list_2.insert(1,"樊哥来了")
print(f"插入元素后，列表为{list_2}")
#追加元素到末尾  方法： 列表.appene(元素) 单个元素
list_2.append('全是牛马')
print(f"追加元素后，列表为{list_2}")
#追加一批元素
#语法：列表.extend(其他数据容器)
list_2.extend(new_list)
print(f"追加其他容器后为{list_2}")
