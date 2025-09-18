import math

def calculate_factorial():
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            print("Factorial is not defined for negative numbers!")
        else:
            result = math.factorial(num)
            print(f"Factorial: {result}")
    except ValueError:
        print("Please enter a valid integer!")

def solve_compound_interest():
    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter rate of interest (in %): "))
        time = float(input("Enter time (in years): "))
        
        amount = principal * (1 + rate/100) ** time
        compound_interest = amount - principal
        
        print(f"Compound Interest: {compound_interest:.2f}")
        
    except ValueError:
        print("Please enter valid numbers!")

def trigonometric_calculations():
    try:
        angle_degrees = float(input("Enter angle in degrees: "))
        angle_radians = math.radians(angle_degrees)
        
        print(f"Sin: {math.sin(angle_radians):.4f}")
        print(f"Cos: {math.cos(angle_radians):.4f}")
        print(f"Tan: {math.tan(angle_radians):.4f}")
        
    except ValueError:
        print("Please enter a valid number!")

def calculate_area():
    print("\nArea Calculation Options:")
    print("1. Circle  2. Rectangle  3. Triangle  4. Square")
    
    choice = input("Choose a shape: ")
    
    try:
        if choice == "1":
            radius = float(input("Enter radius: "))
            area = math.pi * radius ** 2
            print(f"Area of circle: {area:.2f}")
        elif choice == "2":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            area = length * width
            print(f"Area of rectangle: {area:.2f}")
        elif choice == "3":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            area = 0.5 * base * height
            print(f"Area of triangle: {area:.2f}")
        elif choice == "4":
            side = float(input("Enter side length: "))
            area = side ** 2
            print(f"Area of square: {area:.2f}")
        else:
            print("Invalid choice!")
            
    except ValueError:
        print("Please enter valid numbers!")

def math_operations():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            calculate_factorial()
        elif choice == "2":
            solve_compound_interest()
        elif choice == "3":
            trigonometric_calculations()
        elif choice == "4":
            calculate_area()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")
        

        print("=" * 30)
