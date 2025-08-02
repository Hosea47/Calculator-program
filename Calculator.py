#Ask the user to input the desired numbers
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

#Ask the user to input their desired operation
print("Choose one of these operations; + , - , * , / ")
operation = input("You have chosen the operation: ")

#Instructions on how the user's choice should be handled
if operation == "+" :
    result = num1 + num2
elif operation == "-" : 
    result = num1 - num2
elif operation == "*" :
    result = num1 * num2
elif operation == "/" :
    if num2 != 0 : 
        result = num1 / num2
    else :
        result = "Oops you cannot divide by 0"

else :
    result = "Missing number or operation.Please try again"

#Displaying the result 
print("Your result is : ",result)