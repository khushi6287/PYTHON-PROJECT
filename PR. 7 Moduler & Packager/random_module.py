import random
import string

def generate_random_number():
    try:
        min_val = int(input("Enter minimum value: "))
        max_val = int(input("Enter maximum value: "))
        result = random.randint(min_val, max_val)
        print(f"Random number: {result}")
    except ValueError:
        print("Please enter valid numbers!")

def generate_random_list():
    try:
        size = int(input("Enter list size: "))
        min_val = int(input("Enter minimum value: "))
        max_val = int(input("Enter maximum value: "))
        
        random_list = [random.randint(min_val, max_val) for _ in range(size)]
        print(f"Random list: {random_list}")
    except ValueError:
        print("Please enter valid inputs!")

def create_random_password():
    try:
        length = int(input("Enter password length: "))
        
        if length < 1:
            print("Password length must be at least 1!")
            return
            
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ''.join(random.choice(chars) for _ in range(length))
        print(f"Generated Password: {password}")
        
    except ValueError:
        print("Please enter a valid number!")

def generate_random_otp():
    try:
        length = int(input("Enter OTP length (4-8 recommended): "))
        
        if length < 1:
            print("OTP length must be at least 1!")
            return
            
        otp = ''.join(random.choice(string.digits) for _ in range(length))
        print(f"Generated OTP: {otp}")
        
    except ValueError:
        print("Please enter a valid number!")

def random_operations():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            generate_random_number()
        elif choice == "2":
            generate_random_list()
        elif choice == "3":
            create_random_password()
        elif choice == "4":
            generate_random_otp()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")
        

        print("=" * 30)
