##The Famous FizzBuzz
## 1. Print the numbers 0 - 100
## 2. For numbers that are divisible by 3, print "fizz" instead of printing the number.
## 3. For numbers that are divisible by 5, print "Buzz", instead of printing the number.
## 4. For numbers that are diviisible by 3 and 5, print "FizzBuzz", instead of printing the number.

#for newNum in range(101):
 #   print(newNum)


counter = 0

while counter <= 100:
    #For every thing that is divisible by 3 and 5, it has to be divisible by 3*5.
    # could also be written as if counter % 3 == 0 and counter % 5 == 0: 
    if counter % 15 == 0:
        print("FizzBuzz")
    elif counter % 3 == 0:
        print("Fizz")
    elif counter % 5 == 0:
        print("Buzz")

    else:
        print(counter)
    counter += 1



