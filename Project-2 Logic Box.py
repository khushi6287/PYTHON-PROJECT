print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\nSelect an option:")
    print("1.Generate a Pattern")
    print("2.Analyze a Range of Numbers")
    print("3.Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        rows = int(input("\nEnter the number of row for the pattern:  "))
        print("\nPattern:")
        for i in range(1, rows + 1):
            print("*" * i)

    elif choice == "2":
        start = int(input("\nEnter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        total = 0
        for num in range(start, end + 1):
            if num % 2 == 0:
                print(f"Number {num} is Even")
            else:
                print(f"Number {num} is Odd")
            
            total += num

        print(f"\nSum of all number from {start} to {end} is: {total}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


