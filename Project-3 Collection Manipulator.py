print("Welcome To The Student Data Organizer!")

list1 = []

while True:
	
	print("Select an option:")
	print("1. Add Student")
	print("2. Display all Student")
	print("3. Update Student Information")
	print("4. Delete Student")
	print("5. Display Subjects Offered")
	print("6. Exit")

	ch = int(input("Enter Your Choice from 1-6:"))

	if ch == 1:
		print("Enter Student Details:")
		Student_ID = int(input("Enter Student Id:"))
		Name = input("Enter Name:")
		Age = int(input("Enter Age:"))
		Grade = input("Enter Grade:")
		DOB = input("Date Of Birth (DD-MM-YYYY):")
		subject = set(input("Subjects (comma-seprated):").split(','))

		student = {
				"ID": Student_ID,
				"Name": Name,
				"Age": Age,
				"Grade": Grade,
				"DOB": DOB,
				"Subjects": subject
		}

		list1.append(student)
		print("Student Added Successfully!")

	elif ch == 2:
		if not list1:
			print("No Student list1 found.")
		else:
			for s in list1:
				print("ID :",Student_ID)
				print("Name :",Name)
				print("Age:",Age)
				print("Grade:",Grade)
				print("DOB:",DOB)
				print("Subjects:",','.join(s["Subjects"]))

	elif ch == 3:
		uid = int(input("Enter student Id To update:"))
		found = False
		for s in list1:
			if s["ID"] == uid:
				found = True
				print("1. Update Age\n2. Update subjects")
				update_choice = input("Choose what to update:")
				if update_choice == "1":
					s["Age"] = int(input("Enter Age:"))
					print("Age Updated.")
				elif update_choice == "2":
					new_subjects = set(input("Enter new subjects(comma-seprated):").split(","))
					s["Subjects"] = new_subjects
					print("subjects Updated.")
				break
		if not found:
			print("Student Id not Found.")

	elif ch == 4:
		uid = int(input("Enter student Id To Delete:"))
		for s in list1:
			if s["ID"] == uid:
				list1.remove(s)
				print("student record deleted.")
				break
			else:
				print("student Id not Found.")

	elif ch == 5:
		all_subjects = set()
		for s in list1:
			all_subjects.update(s["Subjects"])
			print("Subjects Offered:",','.join(all_subjects))

	elif ch == 6:
		print("Thank you for using the student data Organizer.GoodBye!")
		break

	else:
		print("Invalid Choice! Please try again.")

