def euclidean_algorithm(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = 100
num2 = 5
gcd = euclidean_algorithm(num1, num2)
print("Наибольший общий делитель чисел", num1, "и", num2, ":", gcd)