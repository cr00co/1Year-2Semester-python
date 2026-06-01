n = int(input("Кол-во человек: "))
k = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {k}-й человек")

circle = list(range(1, n + 1))
idx = 0

while len(circle) > 1:
    print(f"\nТекущий круг людей: {circle}")
    print(f"Начало счёта с номера {circle[idx]}")
    idx = (idx + k - 1) % len(circle)
    print(f"Выбывает человек под номером {circle[idx]}")
    circle.pop(idx)
    if idx == len(circle):
        idx = 0

print(f"\nОстался человек под номером {circle[0]}")