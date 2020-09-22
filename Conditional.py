color = input("What is your favorite color?: ")

#use the "If" keyword to start an if statment followed by a condition to evaluate
if color == "red":
    print("That is my favorite color too!")
elif color == "blue":
    print("That is my favorite color too! Blue is best!")
elif color == "yellow":
    print("That is my favorite color too! Everyone love yellow!")
else:
    print("{} is not my favorite, but it is pretty cool.".format(color))