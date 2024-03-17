'''
class Clock:
    id=None
    price=None

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)

Clock1=Clock()
Clock1.id='0030302'
Clock1.price=19.99
print(f"闹钟id：{Clock1.id},价格：{Clock1.price}")
Clock1.ring()

Clock2=Clock()
Clock2.id='00306302'
Clock2.price=19.996
print(f"闹钟id：{Clock2.id},价格：{Clock2.price}")
Clock2.ring()
'''

'''
class Student:
    def __init__(self,name,age,tel):
        self.name=name
        self.age=age
        self.tel=tel
stu1=Student("周杰伦",32,"13243277540")
print(stu1.name,stu1.age,stu1.tel)
'''
class student:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address=address
for i in range(10):
    name=input("请输入学生姓名：")
    age=int(input("请输入年龄："))
    address=input("请输入地址：")
    stu=student(name,age,address)
    print(stu.name,stu.age,stu.address)








 




















