def Exp_to_sav():    
    print("Lets gather your monthly expenses. \n")
    rent = int(input("Enter your rent: "))
    car = int(input("Enter your car payments: "))
    insurance = int(input("Enter your insurance costs: "))
    medical = int(input("Enter your medical costs: "))
    utilities = int(input("Enter your utility expenses: "))
    other = int(input("Enter any extra expenses you wish to account for: "))

    expenseTotal = rent + car + insurance + medical + utilities + other
    print("\nYour total monthly expenses amount to:", expenseTotal)

    print("\nNow let's gather your income so we can calculate your net earnings.")
    monthOrYear = input("\nWill you want to save an amount each month or each year? (m/y)")
    if monthOrYear == "m":
        income = int(input("\nPlease enter your current monthly income: "))
        saveAmount = int(input("\nSounds good. How much would you like to save monthly?: "))
        howMany = int(input("\nFor how many months?: "))
        monthly = True
        yearly = False
    elif monthOrYear == "y":
        income = int(input("\nPlease enter your current yearly income: "))
        saveAmount = int(input("\nSounds good. How much would you like to save yearly?: "))
        howMany = int(input("\nFor how many years?: "))
        yearly = True
        monthly = False
    else:
        print("\nInvalid Input. Goodbye.")
    
    
    
    if monthly == True:   
        i = 0
        while i < 12:
            i += 1
            if i is 12:
                income = income  - expenseTotal
                print("\nYour remaining funds in checking each month - after expenses and money saved: ", income - saveAmount)
                print("\nYour funds in savings - after", howMany, "months: ", saveAmount * howMany, "\n")
                break
    elif yearly == True:         
        i = 0
        while i < 12:           
            i += 1
            income = income - expenseTotal
            if i is 12:               
                income = income - saveAmount                
                print("\nYour funds in checking after expenses each month and money saved each year: ", income)
                print("\nYour savings after", howMany, "years: ", saveAmount * howMany, "\n")
                break

Exp_to_sav()
