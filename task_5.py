#proceed = int(input("Введите сумму выручки"))
#cost = int(input("Введите сумму издержек"))
proceeds = 123
cost = 7

if proceeds >= cost:
    print("Ваша фирма получила прибыль ", (proceeds - cost))
    print("Рентабельность составила : {:.2f}".format((proceeds - cost) / proceeds * 100), " процентов")
#    staff = int(input("Введите количество сотрудников фирмы "))
    staff = 3
    print("Прибыль на одного сотрудника составила: {:.2f}".format((proceeds - cost) / staff))

else:
    print("Ваша фирма несет убытки")
