def sum(x, y, z):
    total = x + y + z

    if x == y == z:
        return  ( number1 * number2 * number3)
    elif x == y:
        return ( number1 * number2 + number3)
    elif y == z:
        return (number1 + number2 * number3)
    elif x == z:
        return (number1 * number3 + number2)
    else:
        return total

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

result = sum(number1, number2, number3)
print("Result:", result)