# int(x [,base]) 将x转换为一个整数
a = int(1.0) 
print(type(a))

# float(x) 将x转换到一个浮点数
b = float(1) 
print(type(b))

# complex(real [,imag]) 创建一个复数
c = complex(1, 2)
print(type(c))

# str(x) 将对象 x 转换为字符串
d = str(520) 
print(type(d))

# repr(x) 将对象 x 转换为表达式字符串
e = repr({1:'C/C++', 2:'Java', 3:'Python'})
print(type(e))

# eval(str) 用来计算在字符串中的有效Python表达式,并返回一个对象
f = eval('pow(2,10)')
print(f)

# tuple(s) 将序列 s 转换为一个元组
g = tuple([1, 2, 3])
print(g)

# list(s) 将序列 s 转换为一个列表
h = list((1, 2, 3))
print(h)

# set(s) 转换为可变集合
i = set([1, 2, 3])
print(i)

# dict(d) 创建一个字典。d 必须是一个序列 (key,value)元组。
j = dict([(1, 2), (3, 4)]) 
print(j)

# frozenset(s) 转换为不可变集合
k = frozenset([1, 2, 3])
print(k)

# chr(x) 将一个整数转换为一个字符
l = chr(520)
print(l)

# ord(x) 将一个字符转换为它的整数值
m = ord('Ȉ')
print(m)

# hex(x) 将一个整数转换为一个十六进制字符串
n = hex(15)
print(n)

# oct(x) 将一个整数转换为一个八进制字符串
o = oct(10)
print(o)