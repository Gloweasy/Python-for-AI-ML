# Full Name: Glory Mbong
# Date: June 12, 2025
# Project: Smart Calculator with Error Handling, Functions, and History

def calculate (num1, operator, num2):
    if operator =="+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    elif operator == "^":
        return num1 ** num2
    elif operator =="%":
        if num2 == 0:
            return "Error: Cannot perform modulus with zero."
        return num1 % num2 
    else:
        return "Error: Invalid operator"
    
def parse_expression(expression):
    try:
        parts = expression.split() #splits the parts
        if len(parts) != 3:
            return None, None, None
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])
        return num1, operator, num2
    except:
        return None, None, None
    
#History list to store all calculations
history = []
#welcome message
print ("\n Welcome to Glo-Smart Calculator!\n")

#start the loop
while True:
    user_input = input("Enter Calculation (e.g, 2 + 3): ")
    num1, operator, num2 = parse_expression(user_input)

    if num1 is None or operator is None or num2 is None:
        print("Ooops! Invalid input format. Use this format: number operator number (e.g, 2 * 4)")
    else:
        result = calculate(num1, operator, num2)
        print("Result: ", result)
        history.append(f"{num1} {operator} {num2} = {result}") 

    cont = input("\n Do you want to perform another calculation? (yes/no): ").lower()
    if cont != "yes":
        break
    
    print("\n Wow! I'm happy to hear that!\n")
        
#print history before exiting
print("\n Calculation History: ")
for item in history:
    print(" -", item)
print("\n Thank you for using Glo-Smart calculator!\n")
print(" Have a nice day!😊\n")
