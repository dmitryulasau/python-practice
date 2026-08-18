# FLOAT
# bet = int(input("Сколько ставим? "))
# ratio = float(input("Какой коэффициент? "))
# win = round(bet * ratio, 2)

# print(f"Потенциальный выигрыш: {win}")

# ---------------------

# age = int(input("Введите возраст: "))
# temperature = float(input("Введите температуру: "))

# money = round(age * 1.5 * temperature, 2)

# print(money)

# ---------------------

# weight = float(input("Введите вес: "))
# height = float(input("Введите рост: "))

# bmi = round(weight / (height ** 2), 2)

# print(f"Индекс массы тела: {bmi}")

# if bmi < 18.5:
#     print("У вас недобор")
# elif bmi < 25:
#     print("У вас всё хорошо!")
# elif bmi < 30:
#     print("У вас избыток :/")
# else:
#     print("ОЖИРЕНИЕ!")

# ---------------------

# chatl = int(input("Сколько чатлов? "))
# cr = chatl / 2200
# ship = int(cr / 0.5)
# print(f"Это {cr} CR")
# print(f"Можно купить кораблей: {ship}")

# ---------------------

# print("Введите местоположение фигуры")

# while True:
#     x = float(input("По горизонтали: "))
#     y = float(input("По вертикали: "))

#     if x < 0 or y < 0 or x >= 0.8 or y >= 0.8:
#         print("Клетки с такой координатой не существует")
#     else:
#         x_axis = int(x * 10)
#         y_axis = int(y * 10)
#         print(f"Фигура находится в клетке ({x_axis}, {y_axis})")

# ---------------------

print("Введите местоположение фигуры")

while True:
    x = float(input("По горизонтали: "))
    y = float(input("По вертикали: "))


    if x < 0 or y < 0 or x >= 0.8 or y >= 0.8:
        print("Клетки с такой координатой не существует")
    else:
        x_axis = int(x * 10)
        y_axis = int(y * 10)

        x_disorder = (x * 10 - x_axis) / 10
        y_disorder = (y * 10 - y_axis) / 10

        if x_disorder < 0.05:
            x_center = 0.05 - x_disorder
        elif x_disorder > 0.05:
            x_center = -(x_disorder - 0.05)
        else:
            x_center = 0

        if y_disorder < 0.05:
            y_center = 0.05 - y_disorder
        elif y_disorder > 0.05:
            y_center = -(y_disorder - 0.05)
        else:
            y_center = 0

    
        print(f"Фигура находится в клетке ({x_axis}, {y_axis})")
        print(f"Поправьте положение фигуры на ({round(x_center, 3)}, {round(y_center, 3)})")
        break

    



# ---------------------

    


