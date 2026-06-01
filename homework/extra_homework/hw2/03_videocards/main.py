n = int(input("Количество видеокарт: "))
cards = []
for i in range(1, n + 1):
    cards.append(int(input(f"{i} Видеокарта: ")))
 
print(f"Старый список видеокарт: [ {' '.join(map(str, cards))} ]")
 
max_card = max(cards)
while max_card in cards:
    cards.remove(max_card)
 
print(f"Новый список видеокарт: [ {' '.join(map(str, cards))} ]")