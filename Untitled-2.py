my_int = int(input("Enter a positive integer: "))
count = 0

while my_int > 0:
    if my_int % 2 == 1:
        my_int = my_int//2
    else:
        my_int = my_int - 1
    count = count + 1

print(count)
print(my_int)