'''
try:
    print(name,age)
except Exception as e:#获取全部异常
    print(666)
'''

try:
    f=open("E:/python/123.text","r",encoding="UTF-8")
except Exception as e:#接受所有异常
    print("出现异常了,已经处理")
    f = open("E:/python/123.text", "w", encoding="UTF-8")
else:#若无异常，执行
    print("好高兴，没有异常")
finally:
    print("我是finally,有没有异常我都要执行")
    f.close()