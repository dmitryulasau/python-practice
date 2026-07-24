
# bad_grade = 0
# for i in range(5):
#     question = input("Кто написал произведение? ")
#     if question == "Пушкин" or question == "пушкин":
#         print("Верно!")
#         break
#     print('Неправильно!')
#     bad_grade += 1
# print(f"Всего двоек: {bad_grade}")

# -----------------------------------------------------

# while True:
#     question = input("Ты выполнил задание, которое выдали тебе вчера? ")
#     if question == "Да, конечно, сделал":
#         break

# -----------------------------------------------------

# name = input("Как тебя зовут? ")
# print(f"{name}, купи слона!")
# while True:
#     answer = input()
#     print(f"Все говорят {answer}, а ты купи слона!")
    
# for symbol in "Python!":
#     print(symbol)

# -----------------------------------------------------

# text = input("Введите текст: ")
# for symbol in text:
#     print(symbol * 3)

# -----------------------------------------------------

# text = input("Введите текст: ")
# big_letters = 0
# small_letters = 0
# for symbol in text:
#     if symbol == "Ы":
#         big_letters +=1
#     elif symbol == "ы":
#         small_letters += 1

# print(f"Больших букв Ы: {big_letters}")
# print(f"Маленьких букв Ы: {small_letters}")

# -----------------------------------------------------

# for i in range(6):
#     if i == 0 or i == 5:
#         print("-" * 10)
#     else:
#         print("|" + ("0" * 8) + "|")

# -----------------------------------------------------

# number = int(input("Введите число: "))
# step = int(input("Введите шаг: "))
# number_sum = 0
# for i in range(3):
#     print(number, end=".")
#     number_sum += number
#     number += step
# print(number_sum)

# -----------------------------------------------------

number = int(input("Введите число: ")) 
print("-=-", end="") 
for i in range(0, number + 1, 10): 
    print(i, end="-=-")
print()
    