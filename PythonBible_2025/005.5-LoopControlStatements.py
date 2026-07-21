print("\n  ")
print(" ")

"""some statements like break, continue pass allow you to control loop execution flow"""
#BREAK
#terminates and exits the closest enclsing look
print("Break: Terminates and exits the closest enclosing look")
for i in range(10):
    if i>2:
        break
    print(i)
    
print("after break hits directly jumps to the code after loop")

print("\n CONTINUE- Jumps to the next iteration,skipping the code after it for current loop")

for i in range(6):
    if i % 2 != 0: #not evenly divisible by 2
        continue
    print(i)
    
print("Pass")
# a null statement that instructs intrepeter to do nothing used as a placeholder when syntax requires a statement.

test == True

if test == False:
    print("\n do nothing")
    pass # Do nothing. 

#Excercise 1.2.1 -1.2.3:
""""1. Break early from a fruit printing loop if banana is encountered
    2. Continue to next iteration in a look if number is divisible by 7 
    3. Use pass a placeholder for future logic in loops/ conditionals"""


    