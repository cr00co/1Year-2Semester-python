k = int(input("Сдвиг: "))
lst = list(map(int, input("Изначальный список (через пробел): ").split()))
print(f"Изначальный список: {lst}")
 
k = k % len(lst)
lst[:] = lst[-k:] + lst[:-k]
 
print(f"Сдвинутый список: {lst}")