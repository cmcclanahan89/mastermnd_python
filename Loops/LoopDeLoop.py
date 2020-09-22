# This one will print out all the numbers between 0 - 50 while adding x or xx if it odd or even. 
x = 0
while x <= 50:
    if x % 2 == 0:
        print(f'{x} XX')
    elif x <= 50:
        print(f"{x} X")
    else:
        continue   
    x += 1

#This one will show if a number is odd will add 1 to it and then reiterate to see if its even. If it is even, it will double the amount and interate again until the value is less than or equal to 50. 
"""
x = 1
while x <= 50:
    if x % 2 != 0:
        print(x)
        x += 1
    elif x % 2 == 0:
        print(x)
        x += x
    
    else:
        continue
    """