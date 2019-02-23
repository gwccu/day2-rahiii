number = int(input("Choose a number"))

remainder = number % 2
if remainder > 0:
    print("number is odd")
else:
    print("number is even")

number1 = int(input("Choose a number"))
number2 = int(input("Choose another number"))
number3 = int(input("Choose a number one last time"))

remainder1 = number1 % 2
if remainder1 > 0:
    print(str(number1) + "is odd")
else:
    print(str(number1) + "is even")

remainder2 = number2 % 2
if remainder2 > 0:
    print(str(number2) + "is odd")
else:
    print(str(number2) + "is even")

remainder3 = number3 % 2
if remainder3 > 0:
    print(str(number3) + "is odd")
else:
    print(str(number3) + "is even")

print("How much do you love animals?")

pet = input("Do you have a pet?")
if pet == "yes":
    points += 1
else:
    points += 0

zoo = input("Have you ever been to the zoo in the last 2 months?")
if zoo == "yes":
    points += 1
else:
    points += 0

donation = input("Have you donated to a animal foundation before?")
if donation == "yes":
    points += 1
else:
    points += 0

