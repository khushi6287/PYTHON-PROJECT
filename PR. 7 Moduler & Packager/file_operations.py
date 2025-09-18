import os

def create_file():
    try:
        filename = input("Enter file name: ")
        with open(filename, 'w') as file:
            file.write("")
        print("File created successfully!")
    except Exception as e:
        print(f"Error creating file: {e}")

def write_to_file():
    try:
        filename = input("Enter file name: ")
        data = input("Enter data to write: ")
        with open(filename, 'w') as file:
            file.write(data)
        print("Data written successfully!")
    except Exception as e:
        print(f"Error writing to file: {e}")

def read_from_file():
    try:
        filename = input("Enter file name: ")
        with open(filename, 'r') as file:
            content = file.read()
        print("File Content:")
        print(content)
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"Error reading file: {e}")

def append_to_file():
    try:
        filename = input("Enter file name: ")
        data = input("Enter data to append: ")
        with open(filename, 'a') as file:
            file.write(data + "\n")
        print("Data appended successfully!")
    except Exception as e:
        print(f"Error appending to file: {e}")

def file_operations():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_file()
        elif choice == "2":
            write_to_file()
        elif choice == "3":
            read_from_file()
        elif choice == "4":
            append_to_file()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")
        

        print("=" * 30)
