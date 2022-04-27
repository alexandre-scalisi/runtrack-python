power = lambda num, pow: 1 if pow <= 0 else num * power(num, pow-1)

print(power(3,3))