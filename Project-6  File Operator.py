from datetime import datetime

class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        entry = input("Enter your journal entry:\n")
        with open(self.filename, "a") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n{entry}\n\n")
        print("Entry added successfully!\n")

    def view_entries(self):
        with open(self.filename, "r") as f:
            content = f.read()
            print("Your Journal Entries:\n" + content)

    def search_entry(self):
        keyword = input("Enter a keyword to search: ")
        with open(self.filename, "r") as f:
            entries = f.read().split("\n\n")
            found = [entry for entry in entries if keyword.lower() in entry.lower()]
            if found:
                print("Matching Entries:\n" + "\n\n".join(found))
            else:
                print(f"No entries found for: {keyword}\n")

    def delete_entries(self):
        confirm = input("Are you sure you want to delete all entries? (yes/no): ")
        if confirm.lower() == "yes":
            open(self.filename, "w").close()
            print("All journal entries deleted.\n")

def main():
    j = JournalManager()
    while True:
        print("\nWelcome to Personal Journal Manager!")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            j.add_entry()
        elif choice == "2":
            j.view_entries()
        elif choice == "3":
            j.search_entry()
        elif choice == "4":
            j.delete_entries()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")

main()



