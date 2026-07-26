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

for row in range(0, 10):
    for col in range(0, -10, -1):
        print(row + col, end="\t")
    print()

