print("\n  ")
print(" ")

#While Executes a code block repeatedly as long a condition is true.

"""while condition: 
#code block will run here."""

print ("Example print 0 to 4")
x=0
while x<5:
    print(x)
    x+=1 # Do not forget to put the increment x

#Conditions is checked first before loop body runs
#Useful When number of iterations isn't know beforehead. 

print ("\nEXCERCISE 1- print squares from 1 to 10 using a while and print")
squares=0
while squares<10:
     print(squares**2)
     squares+=1
     
     
print ("\nsum integers entered by user until 0 is entered")
total=0
number=int(input("Enter an integer (0 to stop): "))
while number !=0:
    total+=number
    number=int(input("Enter an integer (0 to stop): "))
print("The total is:", total)

#While else also supports an optional else block that runs if look exits normally

print("While also supports an optional else borck that runs if look exits normally")
x=5
while x>0:
    print(x)
    x-=1
else: 
    print("countdown finished")
    
#else wont execute if while loop stops due to break

print("\n Excerise 1 - break early from while loop to skip else execution")


print("\n  Excercise 2 - Print numbers from 5 down to 1 using while/else")

print("=== WHILE/ELSE EXERCISE ===")
print("Demonstrating two scenarios:")
print("1. Breaking early to skip else")
print("2. Counting down 5 to 1 with else\n")

# ============================================
# PART 1: BREAK EARLY FROM WHILE LOOP
# ============================================
print("PART 1: Breaking early to skip else execution")
print("-" * 40)

print("Scenario A: Normal loop (else will execute):")
count = 1
while count <= 5:
    print(f"  Processing item #{count}")
    count += 1
else:
    print("  ✅ Loop completed normally - else executed\n")

print("Scenario B: Breaking early (else will NOT execute):")
count = 1
break_point = 3  # We'll break at this point

while count <= 5:
    print(f"  Processing item #{count}")
    
    # Check if we should break early
    if count == break_point:
        print(f"  ⏹️ Breaking early at item #{break_point}")
        break
    
    count += 1
else:
    print("  This message won't appear due to break")

print("\n" + "="*50 + "\n")


#EXCERCISE 1.1.2.1:

# ============================================
# PART 2: COUNTDOWN 5 TO 1 USING WHILE/ELSE
# ============================================
print("PART 2: Countdown from 5 to 1 using while/else")
print("-" * 40)

print("Countdown starting...")
number = 5  # Start from 5

while number >= 1:  # Continue while number is 1 or greater
    print(f"  {number}")
    number -= 1  # Decrement by 1
else:
    print("  🎯 Countdown complete! Else clause executed.")
    print(f"  Final number value: {number}")

print("\n" + "="*50 + "\n")

# ============================================
# BONUS: PRACTICAL EXAMPLE
# ============================================
print("BONUS: Practical Example - Download Manager")
print("-" * 40)

print("Simulating file download with retry logic...")

max_retries = 5
current_try = 1
success = False

while current_try <= max_retries:
    print(f"\n  Attempt {current_try}/{max_retries}")
    print(f"  Downloading...")
    
    # Simulate random success/failure
    import random
    if random.choice([True, False, False]):  # 33% success rate
        print("  ✅ Download successful!")
        success = True
        break
    
    print("  ❌ Download failed")
    
    if current_try < max_retries:
        print(f"  Waiting 1 second before retry...")
        import time
        time.sleep(1)  # Small delay
    
    current_try += 1
else:
    print("\n  ⚠️ Maximum retries reached without success")
    print("  The 'else' clause runs because no 'break' was hit")

# Show final status
if success:
    print("\n  🎉 Proceeding with file processing...")
else:
    print("\n  💔 Download failed. Please try again later.")
    
    