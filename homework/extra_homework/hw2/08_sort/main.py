lst = list(map(int, input("Изначальный список (через пробел): ").split()))
print(f"Изначальный список: {lst}")
 
n = len(lst)
for i in range(n):
    for j in range(0, n - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
 
print(f"Отсортированный список: {lst}")