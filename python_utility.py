def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"


def multiplication_table(number):
    for i in range(1, 13):
        print(number, "x", i, "=", number * i)


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def main():
    while True:
        print("\n===== PYTHON UTILITY MENU =====")
        print("1. Grade Calculator")
        print("2. Multiplication Table")
        print("3. Temperature Converter")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        try:
            if choice == "1":
                score = float(input("Enter your score: "))

                if score < 0 or score > 100:
                    print("Score must be between 0 and 100.")
                else:
                    print("Your grade is:", calculate_grade(score))

            elif choice == "2":
                number = float(input("Enter a number: "))
                multiplication_table(number)

            elif choice == "3":
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print("Temperature in Fahrenheit:", fahrenheit)

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please choose 1-4.")

        except ValueError:
            print("Error: Please enter a valid number.")


main()