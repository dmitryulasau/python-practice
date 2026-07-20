# n = int(input("Введите число: "))
# for i in range(1, n // 2 + 1):
#     print(f"{i * 2} ** 3 = {(i * 2) ** 3}")

# -------------------------------------------

# hours = int(input("Количество часов: "))
# cells = 1
# for i in range(1, hours // 3 +1):
#     hours_elapsed = i * 3
#     cells *= 2
#     hours_left = hours - hours_elapsed
#     print(f"Прошло часов: {hours_elapsed}")
#     print(f"Количество клеток: {cells}")
#     print(f"Осталось часов: {hours_left}")
#     print("________________________________")

# -------------------------------------------

n = int(input("Введите число: "))
for i in range(0, (n + 1) // 2):
    odd = 2 * i + 1
    print(f"{odd} ** 2 = {odd ** 2}")
    