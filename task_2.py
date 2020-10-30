# user_list = []
# n = int(input('Укажите колличество элементов в списке- '))
# position = 1
# for i in range(n):
#     new_element = input("элемент № {} ".format(position))
#     user_list.append(new_element)
#    position += 1
user_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

i = len(user_list)

for elem in range(1, i, 2):
    user_list[elem], user_list[elem - 1] = user_list[elem - 1], user_list[elem]

print(user_list)
