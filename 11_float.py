# FLOAT
bet = int(input("Сколько ставим? "))
ratio = float(input("Какой коэффициент? "))
win = round(bet * ratio, 2)

print(f"Потенциальный выигрыш: {win}")