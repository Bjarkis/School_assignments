n = int(input("Enter the length of the sequence: ")) # Do not change this line

#Create a code that adds the sequence together

#have a sum that adds the previous 3 ints together

#use the for loop to print the numbers, where n is the highest value
    #have add here where the i and sum add toghether

sum_int = 0

first = 1
second = 2
third = 3
 
for i in range(1, n+1):
    if i <= 3:
        print(i)
    else:
        sum_int = first + third + second
        first = second
        second = third
        third = sum_int
        #sum_int = first + third + second

        print(sum_int)

