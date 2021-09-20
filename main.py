"""
作者：JS
时间：2021年09月20日
"""
import time

key_words = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
             'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
             'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static',
             'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']

# 输入文件访问路径
file_name = input("input the file name")

# 输入完成等级
grade = input("input the class")

# 读入文件并将文本分成多行存储在字符串数组内
with open(file_name, encoding = 'utf-8') as c_text:
    lines = c_text.readlines()

# 统计关键字个数
count = 0
chars = ['(', ')', '{', '}', ':', ',', '<', '>', '=', '+', '-', '#', ';']
# 将所有特殊字符换为空格
for line in lines:
    for char in chars:
        line = line.replace(char, ' ')
    # 按空格分词
    words_line = line.split()
    # 对所有分词组遍历
    for word in words_line:
        if word in key_words:
            count+=1
print(count)
