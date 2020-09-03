print("Welcom to car rentals!")
continue_str = str(input("Would you like to continue (y/n)? "))

while continue_str == "y":
    customer_code = str(input("Customer code (b or d): "))
    if customer_code == "b":
        days = int(input("Number of days: "))
        budget_base = 40*days

        odo_start = int(input("Odometer reading at the start: "))
        odo_end = int(input("Odometer reading at the end: "))
        budget_milage = 0.25*(odo_end - odo_start)

        print("Miles driven:", odo_end - odo_start)
        print("Amount due:",round(budget_base + budget_milage, 1))
        