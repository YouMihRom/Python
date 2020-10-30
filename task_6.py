goods = []
number = 1
while input('Желаете добавить товар ? да/нет ') == 'да':
    name_name = input('Название товара: ')
    name_value = int(input('Стоимость товара: '))
    name_units = input('Единицы измерения: ')
    number_units = int(input('Введите количество: '))
    names = {'Название': name_name, 'Цена': name_value, 'Кол-во': number_units, 'ед.': name_units}
    goods.append(tuple([number, names]))
    number += 1
print(goods)
#[(1, {'Название': 'ром', 'Цена': 13, 'Кол-во': 45, 'ед.': 'бочка'}), (2, {'Название': 'лён', 'Цена': 23, 'Кол-во': 89, 'ед.': 'метр'})]

collation_all = {}
for good in goods:
    for name_name, name_value in good[1].items():
        if name_name in collation_all:
            collation_all[name_name].append(name_value)
        else:
         collation_all[name_name] = [name_value]
print(collation_all)
#{'Название': ['ром', 'лён'], 'Цена': [13, 23], 'Кол-во': [45, 89], 'ед.': ['бочка', 'метр']}
