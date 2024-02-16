'''
3. print the multiplication table for given number up to 10, but skip for fifth iteration.

'''
number = 7

for i in range(1,11):
     if i == 5: # skip the 5th iteration
         continue # it will continue to next iteration
     print(number, 'x', i, '=', number * i)
    
