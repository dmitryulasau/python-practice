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

weight = float(input("Введите вес: "))
height = float(input("Введите рост: "))

bmi = round(weight / (height ** 2), 2)

print(f"Индекс массы тела: {bmi}")

if bmi < 18.5:
    print("У вас недобор")
elif bmi < 25:
    print("У вас всё хорошо!")
elif bmi < 30:
    print("У вас избыток :/")
else:
    print("ОЖИРЕНИЕ!")
