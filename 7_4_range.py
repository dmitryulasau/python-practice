# for number in range(1, 11):
#     print(number ** 3)

# -------------------------------------------

# first_number = int(input("Введите первое число: "))
# second_number = int(input("Введите второе число: "))
# result = 0
# for number in range(first_number, second_number + 1):
#     result += number
# print(f"Сумма чисел от {first_number} до {second_number} равна {result}")

# -------------------------------------------

hour_start = int(input("Во сколько Алексей начал свой рабочий день? "))
hour_work = 0
min_activity = 0

for number in range(hour_start, 21):
    
    hour_work += 1
    print(f"{hour_work}-й час")

    activity = int(input("Сколько минут была активность? "))
    min_activity += activity

    if min_activity >= 45:
        break
print(f"Общее время активности: {min_activity} минут. \nРабочих часов: {hour_work}")
