students = []   
subjects = set()  

while True:
    print("\nWelcome to the Student Data Organizer !!!")
    print("\n1. Add Student")
    print("2. Show All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Show All Subjects")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\nEnter Students details:")
        sid = input("Student ID: ")
        name = input("Name: ")
        age = input("Age: ")
        grade = input("Grade: ")
        dob = input("Date of Birth: ")
        sub = input("Subjects (for-eg: Maths, english, ...): ").split(",")

        subjects.update(sub)

        student = {
            "id": sid,
            "name": name,
            "age": age,
            "grade": grade,
            "dob": dob,
            "subjects": sub
        }
        students.append(student)
        print("\nStudent added successfully!!!")

    elif choice == "2":
         for s in students:
                print(f"{s['id']} | {s['name']} | {s['age']} | {s['grade']} | {s['dob']} | {', '.join(s['subjects'])}")
         else:
                print("No students found.")

    elif choice == "3":
        sid = input("\nEnter Student ID to update: ")
        for s in students:
            if s["id"] == sid:
                s["age"] = input("New Age: ")
                s["grade"] = input("New Grade: ")
                s["subjects"] = input("New Subjects (for-eg: Maths, english, ...): ").split(",")
                subjects.update(s["subjects"])
                print("Student updated!!!")
                break
        else:
            print("ID not found.")

    elif choice == "4":
        sid = input("\nEnter Student ID to delete: ")
        for s in students:
            if s["id"] == sid:
                students.remove(s)
                print("Student deleted.")
                break
        else:
            print("ID not found.")

    elif choice == "5":
        if subjects:
            print("\nSubjects:", ", ".join(subjects))
        else:
            print("No subjects added yet.")

    elif choice == "6":
        print("\nGoodbye!!!")
        break

    else:
        print("Invalid choice, try again.")

