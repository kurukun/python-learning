"""
json数据和Python字典的转化
"""
# 导入内置模块json
import json
# 准备数据
data = [{"name": "张一山", "age": 11}, {"name": "王小虎", "age": 12}, {"name": "赵一鸣", "age": 21}]
print(data)
# 将P数据转化为J数据 使用json.dumps()
json_str = json.dumps(data, ensure_ascii=False)  # 有中文时要加入后面的参数，意思为不适用ASCII码去转换它
# 可见json本质上是字符串
print(type(json_str))
print(json_str)
d = {"name": "周杰伦", "age": 12, "skill": "唱歌"}
d = json.dumps(d, ensure_ascii=False)
print(type(d))
print(d)
# 将J数据转化为P数据 使用json.loads()
s = '[{"name": "张一山", "age": 11}, {"name": "王小虎", "age": 12}, {"name": "赵一鸣", "age": 21}]'
l = json.loads(s)
print(type(l))
print(l)