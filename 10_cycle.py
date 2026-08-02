# for row in range(1, 10):
#     for col in range(1, 10):
#         print(row * col, end="\t")
#     print()

#----------------------------------------
# number = int(input("Введите число: "))
# for row in range(0, number + 1):
#     for col in range(0, number + 1):
#         print(row + col, end=" ")
#     print()

#----------------------------------------

# for row in range(0, 10):
#     for col in range(0, -10, -1):
#         print(row + col, end="\t")
#     print()

#-----------------------------------------
# size = int(input("Введите размер матрицы: "))

# for row in range(1, size + 1):
#     for col in range(1, size + 1):
#         if row % 2 == 0:
#             print(row, end=" ")
#         else:
#             print(col, end=" ")
#     print("")

#-----------------------------------------

# size = int(input("Введите размер матрицы: "))
# for row in range(1, size + 1):
#     for col in range(1, size + 1):
#         if col % 3 == 0:
#             print(col, end=" ")
#         else:
#             print(row, end=" ")
#     print()

#-----------------------------------------
# for row in range(20):
#     for col in range(50):
#         if row == 9:
#             print("-", end="")
#         elif col == 24:
#             print("|", end="")
#         else:
#             print(" ", end="")
#     print()

#------------------ GATE -----------------------

# for row in range(20):
#     for col in range(30):
#         if row == 0:
#             print("-", end="")
#         elif col == 0:
#             print("|", end="")
#         elif col == 29:
#             print("|", end="")
#         else:
#             print(" ", end="")
#     print()

#------------------ RACE -----------------------
# for row in range(20):
#     for col in range(50):

#         if col == row + 29:
#             print("\\", end="")
#         elif col == -row + 19:
#             print("/", end="")
#         if row == 9:
#             print("-", end="")    
#         elif col == 24:
#             print("|", end="")
#         else:
#             print(" ", end="")
#     print()

#------------------ MATRIX -----------------------
# size = 5
# for row in range(size):
#     for col in range(size):
#         if row + col == size - 1:
#             print(1, end=" ")
#         elif row + col > size - 1:
#             print(2, end=" ")
#         else:
#             print(0, end=" ")
#     print()

#------------------ QUEUE -----------------------
# number = int(input("Сколько людей в очереди: "))
# for hour in range(number):
#     print(f"*** {hour} час ***")
#     for i in range(hour, number):
#         print(f"Номер в очереди: {i}")
#     print()
# print("Очередь обслужена!")

#------------------ SEQ -------------------------

# number = int(input("Количество чисел в последовательности: "))
# result = 0

# while number > 0:
#     user_number = int(input("Введите число: "))
#     if user_number > 5:
#         result += 1
#     number -= 1
# print(f"Результат: {result}")

#------------------ LADDER -------------------------
# size = int(input("Введите размер матрицы: "))
size = 5
for row in range(size + 1):
    for col in range(row, size + 1):
        print(col, end=" ")
    print()
