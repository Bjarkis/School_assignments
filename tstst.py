num_int = int(input("Find the square root of integer: "))
guess_flt = float(input("Initial guess: "))
tolerance_flt = float(input("What tolerance: "))

original_guess_flt = guess_flt
count_int = 0
previous_flt = 0

while abs(previous_flt - guess_flt) > tolerance_flt:
    previous_flt = guess_flt
    quotent_flt = num_int / guess_flt
    count_int = count_int + 1

print()
print("Square root of", num_int, " is: ", guess_flt)
print("Took ", count_int, " reps to get it to tolerance: ", tolerance_flt)
print("starting from a guess of: ", original_guess_flt)