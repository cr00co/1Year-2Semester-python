guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
MAX = 6

while True:
    print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
    action = input("Гость пришёл или ушёл? ")

    if action == "Пора спать":
        print("\nВечеринка закончилась, все легли спать.")
        break

    name = input("Имя гостя: ")

    if action == "пришёл":
        if len(guests) < MAX:
            guests.append(name)
            print(f"Привет, {name}!\n")
        else:
            print(f"Прости, {name}, но мест нет.\n")
    elif action == "ушёл":
        guests.remove(name)
        print(f"Пока, {name}!\n")