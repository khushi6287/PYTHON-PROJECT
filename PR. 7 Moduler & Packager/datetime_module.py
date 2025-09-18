import datetime
import time

def display_current_datetime():
    now = datetime.datetime.now()
    print(f"Current Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    return now

def calculate_date_difference():
    try:
        print("Enter the first date (YYYY-MM-DD): ", end="")
        date1_str = input()
        print("Enter the second date (YYYY-MM-DD): ", end="")
        date2_str = input()
        
        date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d')
        
        difference = abs((date2 - date1).days)
        print(f"Difference: {difference} days")
        
    except ValueError:
        print("Invalid date format! Please use YYYY-MM-DD format.")

def format_custom_date():
    try:
        date_str = input("Enter date (YYYY-MM-DD): ")
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        
        print("Custom date formats:")
        print(f"1. Full format: {date_obj.strftime('%A, %B %d, %Y')}")
        print(f"2. Short format: {date_obj.strftime('%m/%d/%y')}")
        print(f"3. ISO format: {date_obj.strftime('%Y-%m-%d')}")
        
    except ValueError:
        print("Invalid date format! Please use YYYY-MM-DD format.")

def stopwatch():
    start_time = time.time()
    input("Press Enter to stop stopwatch...")
    end_time = time.time()
    elapsed = end_time - start_time
    print(f"Elapsed time: {elapsed:.2f} seconds")

def countdown_timer():
    try:
        seconds = int(input("Enter countdown time in seconds: "))
        print(f"Countdown starting for {seconds} seconds...")
        
        for i in range(seconds, 0, -1):
            print(f"Time remaining: {i} seconds", end="\r")
            time.sleep(1)
        
        print("\nTime's up!")
        
    except ValueError:
        print("Please enter a valid number!")

def datetime_operations():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_current_datetime()
        elif choice == "2":
            calculate_date_difference()
        elif choice == "3":
            format_custom_date()
        elif choice == "4":
            stopwatch()
        elif choice == "5":
            countdown_timer()
        elif choice == "6":
            break
        else:
            print("Invalid choice!")
        

        print("=" * 30)
        
