Sure, here are two programs in Python which achieve the same goal:

Program 1:
```python
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("GCD of two numbers is", gcd(num1, num2))
```

Program 2:
```python
def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("GCD of two numbers is", gcd(num1, num2))
```

Both programs use the same method name `gcd` and take two integer parameters `a` and `b`. The first program uses recursion to apply the Euclidean algorithm, while the second program uses a while loop. Either program will return the greatest common divisor of the two input integers.