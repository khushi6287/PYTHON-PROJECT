import datetime_module
import math_module
import random_module
import uuid_module
import file_operations

def display_menu():
    print("=" * 30)
    print("Welcome to Multi-Utility Toolkit")
    print("=" * 30)
    print("Choose an option:")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")
    print("=" * 30)

def explore_module_attributes():
    module_name = input("\nEnter module name to explore: ")
    try:
        module = __import__(module_name)
        print(f"\nAvailable Attributes in {module_name} module:")
        print(dir(module))
    except ImportError:
        print(f"Module '{module_name}' not found.")
    except Exception as e:
        print(f"Error exploring module: {e}")

def main():
    while True:
        try:
            display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                datetime_module.datetime_operations()
            elif choice == "2":
                math_module.math_operations()
            elif choice == "3":
                random_module.random_operations()
            elif choice == "4":
                uuid_module.uuid_operations()
            elif choice == "5":
                file_operations.file_operations()
            elif choice == "6":
                explore_module_attributes()
            elif choice == "7":
                print("=" * 30)
                print("Thank you for using the Multi-Utility Toolkit!")
                print("=" * 30)
                exit()
            else:
                print("Invalid choice! Please enter a number between 1-7.")

        except KeyboardInterrupt:
            exit("\n\nProgram interrupted by user.")
        except Exception as e:
            print(f"An error occurred: {e}")


main()
