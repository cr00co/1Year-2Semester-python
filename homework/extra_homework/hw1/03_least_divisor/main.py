def least_divisor(n):
    for i in range(2, n+1):
        if n % i == 0:
            return i
        
if __name__ == "__main__":
    n = int(input("Введите число: "))
    print(f"Наименьший делитель, отличный от единицы: {least_divisor(n)}")