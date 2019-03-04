# 数据拼接
# 方法：用"+"号将数据进行拼接
# 目的：数据整合
# 注意：只能将字符串与字符串拼接

name = 'python'
age = 29
print('my name is ' + name + '\nmy age is ' + str(age))
print('my name is %s\nmy age is %d' %(name, age))
print('my name is {}\nmy age is {}'.format(name, age))