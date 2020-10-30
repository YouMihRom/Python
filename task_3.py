year_season = {"winter": (12, 1, 2), "spring": (3, 4, 5), "summer": (6, 7, 8), "autumn": (9, 10, 11)}
seasons = ['зима', 'весна', 'лето', 'осень']
#month = int(input("Введите номер месяца "))
month = 10

if month < 3 or month == 12:
    print(seasons[0])
elif 3 <= month < 6:
    print(seasons[1])
elif 6 <= month < 9:
    print(seasons[2])
elif 9 <= month < 12:
    print(seasons[3])

for i in year_season.keys():
    if month in year_season[i]:
        print(i)




