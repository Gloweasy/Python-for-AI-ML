#def add_numbers(a, b):
  #  """Returns the sum of two numbers"""
  #  return a + b

#def main():
#    """Main function to execute the number"""
#    num1 = float(input("Enter the first number: "))
#    num2 = float(input("Enter the second number: "))
 #   result = add_numbers(num1, num2)
  #  print (f"The sum of {num1} and {num2} is {result}")

#if __name__ == '__main__':
   # main()

def greet_group(names):
    """Greet each person in the group of people"""
    for name in names:
        print(f"Hello, {name} welcome to class!")

def main():
    """Main function to execute the program"""
    group = (["Alice", "Mercy", "Ruth", "Peace"])
    greet_group(group)

if  __name__ == '__main__':
    main()