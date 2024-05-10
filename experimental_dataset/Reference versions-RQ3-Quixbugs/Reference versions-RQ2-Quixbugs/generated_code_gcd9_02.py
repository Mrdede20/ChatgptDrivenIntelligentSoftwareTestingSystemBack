
def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("GCD of two numbers is", gcd(num1, num2))
