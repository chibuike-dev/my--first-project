# ==========================================
# DAY 11 - PYTHON EXERCISES
# ==========================================


# ==========================================
# EXERCISE 1: CREATE VARIABLES
# ==========================================

student_name = "Godswill"
student_age = 19
student_height = 1.75
is_student = True

print("Student Name:", student_name)
print("Student Name Type:", type(student_name))

print("Student Age:", student_age)
print("Student Age Type:", type(student_age))

print("Student Height:", student_height)
print("Student Height Type:", type(student_height))

print("Is Student:", is_student)
print("Is Student Type:", type(is_student))


# ==========================================
# EXERCISE 2: BASIC CALCULATOR
# ==========================================

number1 = float(input("\nEnter the first number: "))
number2 = float(input("Enter the second number: "))

print("\n--- CALCULATOR RESULTS ---")
print("Sum:", number1 + number2)
print("Difference:", number1 - number2)
print("Product:", number1 * number2)

if number2 != 0:
    print("Quotient:", number1 / number2)
    print("Remainder:", number1 % number2)
else:
    print("Quotient: Cannot divide by zero")
    print("Remainder: Cannot divide by zero")


# ==========================================
# EXERCISE 3: TEMPERATURE CONVERTER
# ==========================================

celsius = float(input("\nEnter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Celsius to Fahrenheit:", fahrenheit)

fahrenheit_temperature = float(
    input("\nEnter temperature in Fahrenheit: ")
)

kelvin = (fahrenheit_temperature - 32) * 5 / 9 + 273.15

print("Fahrenheit to Kelvin:", kelvin)


# ==========================================
# EXERCISE 4: ROBOT SENSOR MONITOR
# ==========================================

print("\n--- ROBOT SENSOR MONITOR ---")

robot_name = input("Enter Robot Name: ")
robot_id = input("Enter Robot ID: ")
sensor_name = input("Enter Sensor Name: ")
sensor_reading = float(input("Enter Sensor Reading: "))
operating_limit = float(input("Enter Operating Limit: "))

difference = operating_limit - sensor_reading

print("\n================================")
print("       ROBOT SENSOR REPORT")
print("================================")
print("Robot Name:", robot_name)
print("Robot ID:", robot_id)
print("Sensor Name:", sensor_name)
print("Sensor Reading:", sensor_reading)
print("Operating Limit:", operating_limit)
print("Difference:", difference)
print("================================")