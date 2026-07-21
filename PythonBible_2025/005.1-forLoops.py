#the for loops iterate over items of a sequence and runs a code block once for each item. Sequences like strings, lists, tuples can ve used with for.

''''the for loops  iterate over items of a sequence and runs acode block once for each item. Sequence like strings, lists can be used with for
code 
for item in sequence: 
#clode block '''

fruits  = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I have an",fruit)

person = ["John",30,"New York"]
for value in person:
    print(value)

'''to iterate a fixed number of times instead of over a sequence, use the range () type
for i in range(start,stop,step_size):
'''

for i in range (1,10):
    print (i)

#Start: starting number is (default)
#stop: generate numbers up to , but not including this number
#Step_size:difference between numbers.


