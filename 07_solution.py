'''
7. keep asking the user for input until they enter a number between 1 and 10.
'''


while True:
   number = int(input("Enter the number between 1 and 10:")) 
   if 1 <= number <= 10:
       print("Thank you!")
       break
   else:
       print("Invalid number please try again")