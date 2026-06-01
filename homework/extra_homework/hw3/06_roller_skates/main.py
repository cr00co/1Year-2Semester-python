n = int(input("Кол-во коньков: "))
skates = []
for i in range(1, n + 1):
    skates.append(int(input(f"Размер {i}-й пары: ")))

k = int(input("\nКол-во людей: "))
people = []
for i in range(1, k + 1):
    people.append(int(input(f"Размер ноги {i}-го человека: ")))

skates_copy = skates[:]
count = 0
for size in people:
    if size in skates_copy:
        skates_copy.remove(size)
        count += 1

print(f"\nНаибольшее кол-во людей, которые могут взять ролики: {count}")