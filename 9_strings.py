
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

# number = int(input("Введите число: ")) 
# print("-=-", end="") 
# for i in range(0, number + 1, 10): 
#     print(i, end="-=-")
# print()
    

#------------- PALINDROME ---------------

# text = input("Что написано в свитке? ")
# new_text = ""
# for symbol in text:
#     new_text = symbol + new_text

# if new_text == text:
#     print("Да, это палиндром!")
# else:
#     print("Нет, это не палиндром!")
# print(new_text)


#          1   3   5   7   8   6   4   2
# Слово: | s | a | n | d | w | i | c | h |
# Шифр:  | s | h | a | c | n | i | d | w |
#          1   2   3   4   5   6   7   8

# text = "Введите кодовое слово: " #shacnidw
odd_letters = ""
even_letters = ""
symbol_count = 0

for symbol in "shacnidw":
    symbol_count += 1

    if symbol_count % 2 == 0:
        even_letters = symbol + even_letters
    else:
        odd_letters += symbol

result = odd_letters + even_letters
print(result)




