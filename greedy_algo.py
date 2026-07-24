boys = int(input("Введите количество мальчиков: "))
girls = int(input("Введите количество девочек: "))
answer = ""

if girls * 2 < boys or boys * 2 < girls:
    print("Ответ: Нет решения")
elif boys >= girls:
    k = boys - girls
    for bgb in range(k):
        answer += "BGB"
    for bg in range(girls - k):
        answer += "BG"
else:
    k = girls - boys
    for bgb in range(k):
        answer += "GBG"
    for bg in range(boys - k):
        answer += "GB"

print(answer)
