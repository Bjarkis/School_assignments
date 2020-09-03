year = int(input("Input a year: ")) # Do not change this line

# Fill in the missing code below

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            if year == "366 days":
                print("True")
            else:
                print("True")
        else:
            print("False")
    else:
        print("True")
else:
    print("False")