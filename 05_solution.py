'''
5. Find the first Non-Repeated character
   Given a string, find non-repeated character.
'''
name_str = "teenager"

for i in name_str:
    print(i)
    if name_str.count(i) ==1:
        print("first non-repeated character:",i)
        break