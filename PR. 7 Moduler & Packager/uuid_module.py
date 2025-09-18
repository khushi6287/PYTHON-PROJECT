import uuid

def generate_uuid4():
    unique_id = uuid.uuid4()
    print(f"Generated UUID: {unique_id}")
    return str(unique_id)

def generate_multiple_uuids():
    try:
        count = int(input("Enter number of UUIDs to generate: "))
        
        print(f"\nGenerated {count} UUIDs:")
        for i in range(count):
            unique_id = uuid.uuid4()
            print(f"{i+1:3d}. {unique_id}")
            
    except ValueError:
        print("Please enter a valid number!")

def uuid_for_files():
    filename = input("Enter filename (without extension): ")
    file_uuid = uuid.uuid4()
    print(f"File: {filename}_{file_uuid}.txt")
    print(f"Unique File ID: {file_uuid}")

def uuid_operations():
    while True:
        print("\nGenerate Unique Identifiers:")
        print("1. Generate UUID")
        print("2. Generate Multiple UUIDs")
        print("3. UUID for File Naming")
        print("4. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            generate_uuid4()
        elif choice == "2":
            generate_multiple_uuids()
        elif choice == "3":
            uuid_for_files()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")
        

        print("=" * 30)
