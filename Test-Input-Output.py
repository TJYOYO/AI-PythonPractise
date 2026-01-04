# name = input('your name:')
# gender = input('you are a boy?(y/n)')
#
# welcome_str = 'Welcome to the matrix {prefix} {name}.'
# welcome_dic = {
#     'prefix': 'Mr.' if gender == 'y' else 'Mrs',
#     'name': name
# }
#
# print('authorizing...')
# print(welcome_str.format(**welcome_dic))




a = input("input int a=: ")
# 1
b = input("input int b=: ")
# 2

print('a + b = {}'.format(a + b))
########## 输出 ##############
# a + b = 12
print('type of a is {}, type of b is {}'.format(type(a), type(b)))
########## 输出 ##############
# type of a is <class 'str'>, type of b is <class 'str'>
print('a + b = {}'.format(int(a) + int(b)))
########## 输出 ##############
# a + b = 3
