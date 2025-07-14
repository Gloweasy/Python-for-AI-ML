def hello():
    print("Hello, World!")

hello()

def say_hello():
    print("Hello from inside the function!")

def main():
    print("Now inside main () function")
    say_hello()

if __name__ == '__main__':
    main()

def greet():
    print ("Welcome to Python!")

def main():
    greet()

main()

name = "Glory"

def say_name():
    print("My name is", name)

def main():
    say_name()

if __name__ == '__main__':
    main()

def has_vowel(name):
    if set('aeiou').intersection(name.lower()):
        print("Your name contains a vowel.")
    else:
        print("Your name does not contain a vowel.")

def print_letters(name):
    for letter in name:
        print(letter)

#def main():
    user_input = input("Enter your name: ")
    has_vowel(user_input)
    print_letters(user_input)

if __name__ =='__main__':
    main()

#def greet():
    #print("Hello, Welcome to Python!")

#greet() 

#def greet_person(name):
    #print("Hello,", name, "welcome to python!")
#greet_person("James,")


#def greet_people(names):
    #for name in names: 
        #print("Hello,", name, " Welcome to python!")

#greet_people(["Glory!", "Mike!", "Ada!", "Jerry!"])

def greet_group(names):
    for name in names:
        print("Hello,",name,"Welcome to Python!")

    print("All greetings, done!")

greet_group(["Glory!", "Mike!", "Ada!", "Jerry!"])



