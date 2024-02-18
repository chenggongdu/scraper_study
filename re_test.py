import re

content = 'Xiaoshuaib has 100 bananas'
# 非贪婪模式匹配
res = re.match(r'Xi.*?(\d+).*?s', content)
print(res.group(1))

# 贪婪模式匹配
res = re.match(r'Xi.*(\d+).*s', content)
print(res.group(1))

content = """Xiaoshuaib has 100 
bananas"""
# 匹配包含换行符的任意字符
res = re.match(r'Xi.*?(\d+).*?s', content, re.DOTALL)
print(res.group(1))

content = """Xiaoshuaib has 100 
bananas"""
# 查询匹配成功的第一个结果
res = re.search(r'Xi.*?(\d+).*?s', content, re.DOTALL)
print(res.group(1))

content = """Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;"""
# 查询所有匹配的字符
res = re.findall(r'Xi.*?(\d+).*?s;', content, re.DOTALL)
print(res)

content = """Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;
Xiaoshuaib has 100 bananas;"""
content = re.sub(r'\d+', '250', content)
print(content)

content = "Xiaoshuaib has 100 bananas"
pattern = re.compile(r'Xi.*?(\d+).*s')
res = re.match(pattern, content)

print(res.group(1))
