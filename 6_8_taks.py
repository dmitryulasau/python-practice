# secret_number = int(input("Загадай число от 1 до 100: "))
# medium = 50
# while True:
#     guess = int(input(f"Твоё число равно {medium}? (1 - равно; 2 - больше; 3 - меньше): "))
#     if guess == 1:
#         print("Я угадал!")
#         break
#     elif guess == 3:
#         medium //= 2
#     else:
#         medium = round(medium * 1.5)

left = 1
right = 100


while True:
    medium = (left + right) // 2
    guess = int(input(f"Твоё число {medium}? (1 - равно; 2 - больше; 3 - меньше): "))
    if guess == 1:
        print("Я угадал!")
        break
    elif guess == 2:
        left = medium + 1
    else:
        right = medium - 1
        