n = int(input("Количество контейнеров: "))
containers = []
for _ in range(n):
    w = int(input("Введите вес контейнера: "))
    while w > 200:
        print("Вес не должен превышать 200!")
        w = int(input("Введите вес контейнера: "))
    containers.append(w)

x = int(input("\nВведите вес нового контейнера: "))
while x > 200:
    print("Вес не должен превышать 200!")
    x = int(input("Введите вес нового контейнера: "))

pos = n + 1
for i, w in enumerate(containers):
    if w < x:
        pos = i + 1
        break

print(f"\nНомер, который получит новый контейнер: {pos}")