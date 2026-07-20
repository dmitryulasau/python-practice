n = int(input("Сколько всего карточек? "))
cards_total = 0
for card in range(1, n + 1):
    cards_total += card

my_cards_total = 0
for card in range(1, n):
    card_number = int(input("Введите номер оставшейся карточки: "))
    my_cards_total += card_number

print(f"Номер пропавшей карточки: {cards_total - my_cards_total }")