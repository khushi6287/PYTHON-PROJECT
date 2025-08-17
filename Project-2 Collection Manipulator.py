students_list = []     # list to store student dictionaries
subjects_set = set()   # set to store unique subjects

while True:
    print("\n1. Add Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Subjects")
    print("6. Exit")
    
    ch = input("Enter choice: ")

    if ch == "1":
        sid = input("Student ID: ")
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("DOB : ")
        subjects = input("Subjects : ").split(",")

        subjects_set.update(subjects)
        unique_info = (sid, dob)       
        
        students_list.append({sid: {"name": name, "age": age, "grade": grade, "subjects": subjects, "unique_info": unique_info }})
        print("Student added.")

    elif ch == "2":
        if not students_list:
            print("No records.")
        else:
            for student in students_list:
                for sid, details in student.items():
                    print(f"{sid} | {details['name']} | {details['age']} | {details['grade']} | {details['unique_info'][1]} | {', '.join(details['subjects'])}")
   
    elif ch == "3":
        sid = input("Enter Student ID to update: ")
        found = False
        for student in students_list:
            if sid in student:
                details = student[sid]
                details["age"] = int(input("New Age: "))
                details["grade"] = input("New Grade: ")
                details["subjects"] = [s.strip() for s in input("New Subjects: ").split(",")]
                subjects_set.update(details["subjects"])
                print("Updated.")
                found = True
                break
    
        if not found:
            print("ID not found.")

    elif ch == "4":
        sid = input("Enter Student ID to delete: ")
        for student in students_list:
            if sid in student:
                students_list.remove(student)
                print("Deleted.")
                break
        else:
            print("ID not found.")

    elif ch == "5":
       if subjects_set:
        print("Subjects:", ", ".join(subjects_set))
       else:
        print("No subjects added yet.")

    elif ch == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
