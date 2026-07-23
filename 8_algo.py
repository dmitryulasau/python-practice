# n = int(input("Введите число: "))
# for i in range(1, n // 2 + 1):
#     print(f"{i * 2} ** 3 = {(i * 2) ** 3}")

# -------------------------------------------

# hours = int(input("Количество часов: "))
# cells = 1
# for i in range(1, hours // 3 + 1):
#     hours_elapsed = i * 3
#     cells *= 2
#     hours_left = hours - hours_elapsed
#     print(f"Прошло часов: {hours_elapsed}")
#     print(f"Количество клеток: {cells}")
#     print(f"Осталось часов: {hours_left}")
#     print("________________________________")

# -------------------------------------------

# n = int(input("Введите число: "))
# for i in range(0, (n + 1) // 2):
#     odd = 2 * i + 1
#     print(f"{odd} ** 2 = {odd ** 2}")
    
# -------------------------------------------
# number = int(input("Введите число: "))
# for i in range(1, number + 1, 2):
#     print(f"{i} ** 3 = {i ** 3}")

# -------------------------------------------

# number = int(input("Введите число: "))
# result = 0
# for i in range(1, number + 1, 5):
#     print(f"Номер стула: {i}")
#     result += i
# print(f"Сумма: {result}")

# -------------------------------------------
# wake_up = int(input("Во сколько проснулся Саша? "))
# water = 0
# calories = 0
# for i in range(wake_up, 23, 3):
#     print(f"{i}-й час")
#     water += 1
#     cal = int(input("Сколько съедено калорий: "))
#     calories += cal
# print()
# print("Перед сном итог")
# print(f"Всего калорий: {calories}")
# print(f"Всего литров воды: {water}")

# -------------------------------------------

# seconds = int(input("Введите кол-во секунд: "))
# for second in range(seconds, 0, -1):
#     print(second)
# print("Я иду искать!")

# -------------------------------------------

# while True:
#     year = int(input("Введите год (не меньше 1900): "))
#     if year < 1900:
#         print("Год должен быть не меньше 1900")
#     else:
#         for i in range(year, 1900 - 1, -2):
#             print(i)
#         break

# -------------------------------------------

# seconds = int(input("Сколько секунд считать: "))
# for i in range(seconds - (seconds % 2), 0, -2):   
#     print(i)
# print("Я иду искать!")

# -------------------------------------------

start = 14
end = 9
step = 1

if start < end and step < 1:
    temp = end
    end = start
    start = temp
elif start > end and step >= 1:
    temp = start
    start = end
    end = temp

print(start)
print(end)

for i in range(start, end - 1, step):
    result = (i ** 3) + (2 * i ** 2) - (4 * i) + 1
    print(f"В точке {i} функция равна {result}")