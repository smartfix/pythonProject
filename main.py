print("select * multiply, + add, - minus, / devide")
operator = input("*, +, -, /,  :")
number1 = eval(input("enter the first number......"))
number2 = eval(input("enter the second number....."))

if operator == "*" :
    print(number1 * number2)
elif operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "/":
    print(number1 / number2)
else:
    print("invalid selection " )