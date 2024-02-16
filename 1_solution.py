'''
(1).Counting positive numbers
problem: Given a list of numbers, count how many are positive.
numbers = [1,2,3,-4,5,6,7,-8,9,10]
'''
numbers = [1,2,3,-4,5,6,7,-8,9,10]
positive_number_count = 0
for num in numbers:
   if num > 0:
         positive_number_count += 1
print("final number of positive numbers:",positive_number_count)

''' 
numbers = input("Enter numbers separated by spaces: ")
numbers_list = numbers.split()  # Split the input string into a list of strings
positive_number_count = 0

for num_str in numbers_list:
    num = int(num_str)
    if num > 0:
        positive_number_count += 1

print("Final number of positive numbers is:", positive_number_count)
'''