def fact(n):
    if n == 1 or n == 0:
        return 1
        
    else:
        return n * fact(n - 1)
def dataset_stat(ds):
    Minimum = min(ds)
    Maximum = max(ds)
    Total = sum(ds)
    Average = sum(ds)/len(ds)

    return Minimum, Maximum, Total, Average


print("\n*------Welcome to the Data Analyzer and Transformer Program.------*")
data = []

while True:
    print("\nMain Menu: ")
    print("1. Input Data.")
    print("2. Display Data Summary (Built-in Functions).")
    print("3. Calculate Factorial (Recursion).")
    print("4. Filter Data by Threshold (Lamda Function)")
    print("5. Sort Data.")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")
    choice = (input("\nEnter your choice: "))

    
    if choice == "1":
        arr = input("\nEnter data for 1D array (separated by spaces):")
        for x in arr.split():
            data.append(int(x))
        print("\n Data has been stored successfully!!!")

    elif choice == "2":
        if not data:
            print("\nNo Data available...First Input Data.")
        
        else:           
            print("\nData Summary:")
            print(f"=>Total elements: {len(data)}")
            print(f"=>Minimum value: {min(data)}")
            print(f"=>Maximum value: {max(data)}")
            print(f"=>Sum of all values: {sum(data)}")
            print(f"=>Average value: {sum(data)/len(data)}")

    elif choice == "3":
        n = int(input("\nEnter a number to calculate its factorial: "))
        print(f"\nFactorial of {n} is : {fact(n)}")

    elif choice == "4":
        if not data:
            print("\nNo Data available...First Input Data.")

        else:
            t = int(input("\nEnter a threshold value to filter out data above this value:"))
            check = lambda x : t <= x
            filter_value = []
            for i in data:
                if check(i):
                    filter_value.append(i)
            print(f"\nFiltered Data (values >= {t}): {filter_value}")

        
    elif choice == "5":
        if data:
            print("\nChoose sorting option.")
            print("1. Ascending.")
            print("2. Descending.")
            st_choice = input("\nEnter you choice: ")

            if st_choice == "1":
                print(f"Sorted Data in Ascending order: {sorted(data)}")
            elif st_choice == "2":
                print((f"Sorted Data in Descending order: {sorted(data, reverse = True)}"))
        else:
            print("\nNo Data available...First Input Data.")

    elif choice == "6":
        if data:
            Min, Max, Sum, Avg = dataset_stat(data)
            print("\nData Statistics: ")
            print(f"=>Minimum value: {Min}")
            print(f"=>Maximum value: {Max}")
            print(f"=>Sum of all values: {Sum}")
            print(f"=>Average value: {Avg}")
        
        else:
            print("\nNo Data available...First Input Data.")
        
    elif choice == "7":
        print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye...!!!")
        break
    
    else:
        print("\n\nInvalid Choice.Please Enter valid choice....")


    

