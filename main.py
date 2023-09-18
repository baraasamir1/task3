def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def div(num1, num2):
        return num1 / num2

def mul(num1, num2):
    return num1 * num2

# Test the calculator functions
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Addition:", add(num1, num2))
print("Subtraction:", sub(num1, num2))
print("Division:", div(num1, num2))
print("Multiplication:", mul(num1, num2))