import json

date = [{'name': '张大仙', 'age': '16'}, {'name': '王大锤', 'age': '18'}, {'name': '李艺彤', 'age': '17'}]
json_str = json.dumps(date)
json_str1 = json.dumps(date, ensure_ascii=False)  # 变成json字符串，ensure_ascii=False表示不使用ascii表的形式，确保中文的转换

print(json_str)
print(json_str1)
print(type(json_str))

str_data = '[{"name":"张大仙","age":"16"},{"name":"王大锤","age":"18"},{"name":"李艺彤","age":"17"}]'#注意字符串用双引号
L = json.loads(str_data)#将json变回列表或字典
print(L)
print(type(L))