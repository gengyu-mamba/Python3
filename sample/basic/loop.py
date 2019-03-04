# 循环语句
# break语句 从循环内跳出(必须和if连用)
# continue语句 跳跃到循环开头(必须和if连用)
# pass语句 什么都不做
# else语句 用在循环语句后，如果正常结束循环就执行else语句

loop = ['pass', 'continue', 'break', 'python']
for letter in loop:
    if letter == 'pass':
        print(letter)
        pass
    elif letter == 'continue':
        print(letter)
        continue
    elif letter == 'break':
        print(letter)
        break
    else:
        print(letter)

count = 0
while count < 10:
    print('i love C/C++')
    count += 1
else:
    print('i really love python')