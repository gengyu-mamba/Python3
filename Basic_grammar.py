# print()函数

print('hello world')

print("hello world")

print("Let's play")

print('''hello world!
hello python!''') #换行打印

# 变量和赋值

# 变量命名规范：
# 1、只能是一个词
# 2、只能包含字母、数字和下划线
# 3、不能以数字开头
# 4、尽量描述包含的数据内容

# 数据类型
# 字符串 整数 浮点数

#算术运算符
print(1+2)#加法

print(1-2)#减法

print(1*2)#乘法

print(1/2)#除法

print(2**3)#幂

print(10%3)#取模

print(10//3)#取整数

# 数据拼接
# 方法：用"+"号将数据进行拼接
# 目的：数据整合
# 注意：只能将字符串与字符串拼接

# type() 函数 查询数据类型

#数据转换

# str():将其他数据类型转换为字符串
# int():将其他数据类型转换为整数
# float():将其他数据类型转换为浮点数

#条件判断

# 单项判断：if
# 双向判断：if...else...
# 多项判断：if...elif...else...

#input()函数
content = input('请输入你想输入的内容：')

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

#字典

d = {'QQ':['甲','乙','丙'],123:['A','B','C'],'家':10000}

a = d['QQ'] #取出字典d中的'QQ'键的值,并把这个值赋值给变量a,a被赋值为列表['甲','乙','丙']
b = a[0] #取出列表a中的第0个索引,也就是'甲',并把这个值赋值给变量b
print(b) #打印变量b

print(d[123][1]) #从嵌套中提取元素,d[123]提取出['A','B','C'],d[123][1]提取出'B'

d['家'] = 900 #改变字典中的值
print(d['家'])

d[3.1415926] = '圆周率' #给字典新增键和值
print(d)

print(list(d.values())) #遍历字典中所有的值,可以使用list()来转换为列表

# items()函数以列表返回可遍历的(键,值)元组数组
print(d.items())
for key,value in d.items():
    print('key: {} value: {}'.format(key,value))


# 循环语句
# break语句 从循环内跳出(必须和if连用)
# continue语句 跳跃到循环开头(必须和if连用)
# pass语句 什么都不做
# else语句 用在循环语句后，如果正常结束循环就执行else语句

# 中文 - gbk - url 
import urllib

a= '无名之辈'
b= a.encode('gbk')
# 将汉字，用gbk格式编码，赋值给b
print(b)
print(urllib.parse.quote(b))

# 模块
# 模块：".py"后缀的文件即模块
# import 语句
# 1、import
# 2、import  ... as ...
# 当需要导入多个模块时，可以用逗号隔开。比如：import a,b,c

#  from ... import ...语句

# 格式：
# from (模块名) import (指定模块中的变量名/函数名/类名)
# 效果：
# 1、导入模块中的指定部分(变量名/函数名/类名)
# 2、导入后的指定的部分可以直接使用，无需加上"模块."前缀

# 当我们需要从模块中同时导入多个指定内容，也可以用逗号隔开，写成from xx模块 import a,b,c的形式。
# 当我们需要从模块中指定所有内容直接使用时，可以写成【from xx模块 import *】的形式，*代表“模块中所有的变量、函数、类”

# if __name__ == '__main__'
# 通常在主模块中使用，表示这是"程序的入口"
# xx.py文件：
# 代码块1....
# if __name__ == '__main__':
# 代码块2.......
# 1、当xx.py文件被直接运行时，代码块2将被运行
# 2、当xx.py文件作为模块是被其他程序导入时，代码块2不被运行

# 模块的学习方法
# 1、这模块有哪些函数可用？可以通过dir()函数查询
# 2、有哪些属性或方法可用？去网上看文档或找教程
# 3、使用格式是什么？从文档或教程中搜集案例
