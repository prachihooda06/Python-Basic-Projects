def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    return number1 / number2


def average(number1, number2):
    return (number1 + number2)/2


def power(number1, number2):
    return number1 ** number2


print("Please select operation -\n""1. Add(+)\n""2. Subtract(-)\n""3. Multiply(*)\n"
      "4. Divide(/)\n""5. Average\n""6. Power(**)\n")


select = int(input("Select operations form 1, 2, 3, 4, 5, 6: "))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
    print(number_1, "+", number_2, "=", add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=", multiply(number_1, number_2))

elif select == 4:
    print(number_1, "/", number_2, "=", divide(number_1, number_2))

elif select == 5:
    print("Average of ", number_1, "and", number_2, "=", average(number_1, number_2))

elif select == 6:
    print(number_1, "**", number_2, "=", power(number_1, number_2))
else:
    print("Invalid input")
