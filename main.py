import time,random


print("1- For normal Calculator ")
print("2- For weight converter Kg to L")
print("3- For Countdown Timer")
print("4- For number guessing game ")
print("5- For Rock , Paper and scissors ")
print("6- For Getting information about Python-Libraries")
print("7- For Exchange ")
a = int(input("Which app you want to use ? : "))
#Python Calculator
if a == 1:
    try:
        def add(number1, number2):
            return number1 + number2
        def subtract(number1, number2):
            return number1 - number2
        def multi(number1, number2):
            return number1 * number2
        def divide(number1, number2):
            return number1 / number2
        def power(fake1, fake2):
            result = 1
            for i in range(int(fake2)):
                result *= fake1
                return result
        while True:
            print("\nType \"Exit\" to quit the program\n")
            operator = input("Enter the operator (+ - / *) : ")
            number1 = float(input("Enter the 1st number: "))
            number2 = float(input("Enter the 2nd number : "))
            if operator.lower() == "exit":
                print("The program ended")
                break
            elif operator == "^":
                result = power(number1,number2)
                print(result)
            elif operator == "+":
                result = add(number1, number2)
                print(result)
            elif operator == "-":
                result = subtract(number1 , number2)
                print(result)
            elif operator == "*":
                result = multi(number1, number2)
                print(result)
            elif operator == "/":
                result = divide(number1, number2)
                print(result)
            else:
                print(f"{operator} Is not valid")
    except ValueError as errvalue:
        print(errvalue)

#converter
elif a == 2:
    while True:
        weight = float(input("Enter your weight : "))
        print("\n Enter Exit to quit the program \n")
        unit = input("Kilograms or Pounds? (K or L) : ")
        if unit.upper() == "exit":
            print("Good bye")
            break
        elif unit.upper() == "K":
            weight *= 2.205
            unit = "Pounds"
            print(weight, unit)
        elif unit.upper() == "L":
            weight /= 2.205
            unit = "Kilogram"
            print(round(weight, 1) , unit)
        else:
            print(unit, "Is not Valid, try again")

elif a == 3:
    timee = int(input("Enter the time to countdown : "))
    for x in reversed(range(0 ,timee)):
        second = x % 60
        minute = int(x / 60) % 60
        Hour = int(x / 3600)
        time.sleep(1)
        print(f"{Hour:02}:{minute:02}:{second:02}")
    print("Time is up!")
elif a == 4:
    import random

    from colorama import Fore as F

    low = 1
    high = 10

    answer = random.randint(low, high)
    print(answer)
    is_running = True
    guesses = 0
    print("\n Welcome to number guessing game with python ! \n")
    print(f"Select number between {low} and {high}")
    while is_running:
        guess = int(input(F.MAGENTA + "Enter your guess : "))
        guesses += 1
        if guess == answer:
            print(F.LIGHTYELLOW_EX + "Congrats you won the game !")
            print(f"{answer} Is correct answer")
            print(F.LIGHTGREEN_EX + f"Number of guessing : {guesses}")
            if guesses == 1:
                print(F.BLUE + "You are lucky! Got it on the first try")
            break
        elif guess > 100:
            print(f"Don't be stupid I said from {low} to {high} you entered {guess}")
        elif guess > answer:
            print(F.RED + "The number is bigger than the answer !")
        elif guess < answer:
            print(F.LIGHTWHITE_EX + "The number is smaller than the answer !")

        else:
            print(F.RED + f"{guess} is not number !!")
elif a == 5:
    options = ["PAPER", "ROCK", "SCISSORS"]
    print(f"options is {options}")
    Score = 0
    ai_points = 0
    while True:
        print("Enter \"Exit\" to quit the application 😑")
        ai = random.choice(options)
        Choice = input("You : ").upper()
        if Choice == "EXIT":
            print("Good Bye!")
            break
        elif Choice == options[0] and ai == options[1]:
            print(f"Ai : {ai}")
            print("You won !")
            Score += 1
        elif Choice == ai:
            print(f"Ai : {ai}")
            print("Draw")
        elif Choice == options[0] and ai == options[2]:
            print(f"Ai : {ai}")
            print("You lost ")
            ai_points += 1
        elif Choice == options[1] and ai == options[0]:
            print(f"Ai : {ai}")
            print("You lost")
            ai_points += 1
        elif Choice == options[1] and ai == options[2]:
            print(f"Ai : {ai}")
            print("You won !")
            Score += 1
        elif Choice == options[2] and ai == options[1]:
            print(f"Ai : {ai}")
            print("You lost ")
            ai_points += 1
        elif Choice == options[2] and ai == options[0]:
            print(f"Ai : {ai}")
            print("You won !")
            Score += 1
        else:
            print(Choice.capitalize(), "Is not Valid")

        print(f"Your score is : {Score} and Ai score is : {ai_points}")
elif a == 6:
    import requests

    try:
        library = input("What Library are you searching for : ").lower()

        response = requests.get(f"https://www.piwheels.org/project/{library}/json")
        pypi = response.json()['pypi_url']
        last_release = response.json()['releases']
        summary = response.json()['summary']
        piwheels_url = response.json()['piwheels_url']
        version = ""


        def file():
            filesize = response.json()['releases'][f'{Version}']['released']
            print("The File was upload At : ", filesize)


        print(f"Summary : {summary}")
        print(f"PYPI Link : {pypi}")
        print(f"Piwheels Link : {piwheels_url}")

        Version = input("Enter the version to see the post date : ")
        file()
    except KeyError as key:
        print(f"Error code:1\nDetals: Version {key} Not Found ")
    except requests.exceptions.JSONDecodeError:
        print(f"No Module Named : {library}")
elif a == 7:
    import requests
    while True:

        amount = input("Enter the amount to exchange(\"Exit\" to quit) : ")
        from_currency = "USD"
        to_currency = "IQD"
        if amount.isdigit():
            int(amount)
            url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'

            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                if to_currency in data["rates"]:
                    conversion_rate = data["rates"][to_currency]
                    converted_amount = float(amount) * conversion_rate
                    print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
                else:
                    print(f"Currency {to_currency} not found.")
            else:
                print("Failed to fetch exchange rates.")
        else:
            print(amount, "IS not valid")
        if amount.lower() == "exit":
            print("Good bye")
            break

else:
    print(a,"is invalid")
