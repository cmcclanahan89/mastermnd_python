#For loops only works for things that iterable. An iterable is any Python object capable of returning its members one at a time, permitting it to be iterated over in a for-loop.
# Intergers are not iterable. 

shoppingList = ['apple', 'cokes', 'food', 'ice cream']
adjectives = ['red', 'cold', 'delicous', 'frozen']
"""
for items in shoppingList:
    print(items)
"""
for item in shoppingList:
    for adjective in adjectives:
        print(f"{item} is {adjective}")
   