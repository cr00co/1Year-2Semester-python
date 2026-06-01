shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100],
        ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]

name = input("Название детали: ")

count = sum(1 for item in shop if item[0] == name)
total = sum(item[1] for item in shop if item[0] == name)

print(f"Кол-во деталей — {count}")
print(f"Общая стоимость — {total}")