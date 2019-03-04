#条件判断

# 单项判断：if
# 双向判断：if...else...
# 多项判断：if...elif...else...

age = int(input('How old are you?\n'))
if age <= 0:
    print("You're not even born yet")
elif age < 45:
    print('youth')
elif age < 60:
    print('midlife')
else:
    print('elderly')