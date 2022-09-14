m = int(input("Introduce m: "))
n = int(input("Introduce n: "))

def factorial(y):
    if (y != 1):
        return y * factorial(y - 1)
    else:
        return 1

def combinedfactorial(m, n):
    return (factorial(n) / factorial(m) * factorial(n - m))

print(combinedfactorial(m,n))