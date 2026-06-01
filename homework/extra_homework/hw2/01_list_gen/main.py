N = int(input("Введите число: "))

l = [i for i in range(N + 1) if i % 2 != 0]

print(f"\nСписок из нечётных чисел от одного до N: {l}")