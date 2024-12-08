num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num1, num2 = abs(num1), abs(num2)
a, b = num1, num2
while b != 0:
    a, b = b, a % b

if num1 == 0 or num2 == 0:
    print("LCM of 0 and any number is 0 (undefined case).")
else:
    lcm = (num1 * num2) 
    print(f"LCM of {num1} and {num2} is {lcm}")