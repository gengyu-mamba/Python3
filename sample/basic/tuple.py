# 元组的创建
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
print(tup1)
print(tup2)
print(tup3)

# 空元组
tup1 = ()
print(tup1)

# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
tup1 = (50)
print(type(tup1)) # tup1为整型

tup1 = (50,)
print(type(tup1))

# 访问元组
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )

print('tup1[0]:',tup1[0])
print('tup2[1:5]:',tup2[1:5])

# 修改元组
# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
 
# 以下修改元组元素操作是非法的。
# tup1[0] = 100
 
# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)

# 删除元组
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
tup = ('Google', 'Runoob', 1997, 2000)

print(tup)
del tup

# 元组内置函数

## 计算元组元素个数
tuple1 = ('Google', 'Runoob', 'Taobao')
print(len(tuple1)) 

## 返回元组中元素最大值
tuple2 = ('5', '4', '8')
print(max(tuple2))

## 返回元组中元素最小值
tuple2 = ('5', '4', '8')
print(min(tuple2))

## 将列表转换为元组
list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
tuple1 = tuple(list1)
print(tuple1)