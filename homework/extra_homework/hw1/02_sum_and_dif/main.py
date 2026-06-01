def digit_sum(N):
    return sum(int(i) for i in str(N))

def digit_count(N):
    return len(str(N))

if __name__ == "__main__":
    N = int(input("Введите число: "))
    print(f"\nСумма чисел: {digit_sum(N)}")
    print(f"Количество цифр в числе: {digit_count(N)}")
    print(f"Разность суммы и количества цифр: {digit_sum(N) - digit_count(N)}")

