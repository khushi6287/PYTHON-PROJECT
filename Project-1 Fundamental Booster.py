print("Welcome to the Interactive  Peronal Data collector!!!")

name = input("Please Enter Your Name: ")
age = int(input("Please Enter Your Age: "))
height = float(input("Please Enter Your Height"))
fav_n = int(input("Please Enter Your Favourite Number"))

current_year = datetime.now().year
birth_year = current_year - age
print("\n")
print("Thank You!!! Here is the information we collected:")
print("\n")
print(f"Name: {name} (Type: {type(name)}) (id: {id(name)})")
print(f"Age: {age} (Type: {type(age)}) (id: {id(age)})")
print(f"Height: {height} (Type: {type(height)}) (id: {id(height)})")
print(f"Favourite Number: {fav_n} (Type: {type(fav_n)}) (id: {id(fav_n)})")
print(f"Your Birth Year is: {birth_year}")
