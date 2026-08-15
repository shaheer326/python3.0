try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma : "))
    result = num1 / num2
    print("Result is", result)

except ZeroDivisionError:
    print("Division by zero is error!! ")

except SyntaxError:
    print("Comma is mising. enter the numbers seperated by comma like 1, 2")

except:
    print("Wrong input")

else:
    print("No exeption")

finally:
    print("This will execute no matter what")