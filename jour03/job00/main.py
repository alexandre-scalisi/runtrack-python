factorial = lambda n: 1 if n <= 1 else n * factorial(n - 1)

print(factorial(5))