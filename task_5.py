#new_el = int(input("Введите новое число: "))
new_el = 5
user_list = [8, 6, 4, 3, 2, 2, 2, 1]
for element in user_list:
    if user_list.count(new_el) > 0:
        i = user_list.index(new_el)
        c = user_list.count(new_el)
        user_list.insert(i+c, new_el)
        break
    elif new_el > element:
        pos = user_list.index(element)
        user_list.insert(pos, new_el)
        break
    elif new_el < user_list[len(user_list) - 1]:
        user_list.append(new_el)
print(user_list)
