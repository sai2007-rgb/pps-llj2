try:
    num1 = int(input("Enter the first number (between 1 and 15): "))


    if 1 <= num1 <= 15:
        # Get input from the user for the second number
        try:
            num2 = int(input("Enter the second number (between 1 and 15): "))

          
            if 1 <= num2 <= 15:
                
                try:
                    num3 = int(input("Enter the third number (between 1 and 15): "))

                    if 1 <= num3 <= 15:
                        sum_of_numbers = num1 + num2 + num3
                        print(f"The sum of {num1}, {num2}, and {num3} is {sum_of_numbers}.")
                    else:
                        print("Error: The third number is not in the range of 1 to 15.")
                except ValueError:
                    print("Error: Invalid input. Please enter an integer for the third number.")
            else:
                print("Error: The second number is not in the range of 1 to 15.")
        except ValueError:
            print("Error: Invalid input. Please enter an integer for the second number.")
    else:
        print("Error: The first number is not in the range of 1 to 15.")
except ValueError:
    print("Error: Invalid input. Please enter an integer for the first number.")