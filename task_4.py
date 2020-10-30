# user_list = input("Введите несколько слов через пробел")
# user_list = user_list.split()
user_list = ['one', 'two', 'three', 'four']

for i in user_list:
    print((user_list.index(i) + 1), ' {:.10}'.format(i))



