#user_time = int(input("Введите время в секундах"))
user_time = 22657
var_hour = user_time // (60 * 60)
var_minute = user_time % (60 * 60) // 60
var_second = user_time % (60 * 60) % 60

print(f"Искомое время : {var_hour:02d}:{var_minute:02d}:{var_second:02d}")

