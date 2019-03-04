#列表

s = ['弘福寺', '大兴善寺', '青龙寺', '卧龙寺']

print(s)#打印列表

print(len(s))#打印列表s的长度

print(type(s))#打印列表s的类型

print(s[3])#打印列表s里面的第3个元素

print(s[-2])#打印列表s里面的倒数第2个元素

print(s[0:4])#打印列表s中0、1、2、3的元素

print(s[1:3])#打印列表s中1、2的元素

print(s[1:])#打印列表s中第1个和此之后的所有元素

print(s[:2])#打印列表s中第2个元素之前的所有元素

s.append('观音禅寺')#把数据'观音禅寺'放进列表s的尾部
print(s[4])#打印列表s里面的第4个元素

# 知识1：一种新的列表生成方式
num1 = [1,2,3,4,5]  # 想一想，如果用这个方法生成一个1-100的列表……
num2 = list(range(1,6))
print(num1)
print(num2)

# 知识2：extend 的新用法
num2.extend(['ABCDE'])
num2.extend('ABCDE')  # extend后面是列表的话会将其合并，后面是字符串的话会将每个字符当成一个列表中的元素。
print(num2)

# 知识点3：列表生成式
list1 = [i for i in range(3)]  # 规定列表中元素的范围
print(list1)
list2 = [m+n for m in ['天字', '地字'] for n in '一二']  # 列表元素可以是组合，分别规定范围。
print(list2)
list3 = [n*n for n in range(1,11) if n % 3 == 0]  # 元素既可规定范围，也可附加条件。
print(list3)
