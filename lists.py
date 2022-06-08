ages = []
first_names = []
last_names = []

for i in range(3):
    print()
    print("Please enter your age, name and surname below")
    print()
    ages.append(input("How old are you? "))
    first_names.append(input("What's your name? "))
    last_names.append(input("What's your last name? "))

for person in range(len(first_names)):
    print()
    print(first_names[person] + " " + last_names[person] + " is " + ages[person] + " years old")