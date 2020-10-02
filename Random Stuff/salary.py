start = int(input("What is your starting salary?: "))
raisePercent = int(input("Enter your Raise %: "))
years = int(input("For how many years?: "))

def percentage(x,y):
    return (x * y) / 100

x = 0
for  x in range(0, years):
    newRaise = percentage(start,raisePercent)
    newSal = newRaise + start
    start = newSal
    finalSal = format(newSal, '.2f')
    print(f"year {str(x + 1)}: {finalSal}")
    x + 1

print(f"After {str(x + 1)} years you will have a salary of {finalSal}.")

input()
