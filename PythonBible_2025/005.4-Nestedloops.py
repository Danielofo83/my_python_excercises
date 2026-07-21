print("\n  ")
print(" ")

#you can have nested loops 
print("you can have loops inside other loops to create nested/ multilevel iterations")
for i in range(5):
    for j in range (3):
        print(f" value i {i},value j {j}")
        
        
print("\n this the final of the nested loops")

#Inner Loop runs completely before going to next iteration of outer loop

#very Useful for mulit- dimensional iterations like 2D lists 
print("\n this is the example of a matrix print")

matrix = [[1,2],[3,4]]

for row in matrix: 
    for col in row: 
        print(f"inner col {col}")
     
#EXCERCISE 1.1.3   
#1- PRINT MULTIPLICATION TABLES FROM 2 TO 5 USING NESTED LOOPS

print("=== MULTIPLICATION TABLES (2 to 5) ===")
print("\n simple nested loops")
for table in range(2,6):
    print(f"Multiplication table of {table}:")
    print("-"*50)
    for multiplier in range(1,11):
     result=table*multiplier
     print(f"{table}x{multiplier:2}={result:2}")
    

#2- ITERATE A 2D LIST AND PRINT COORDINATES 

print("\n ==== 2D LIST ITERATION ====")

#create a sample 2 D list (3x3 grid)

grid=["A","B","C","D","E","F"]
print(grid)

#Method 1: Basic nested look with coordinates
print("\n Method 1: Basic nested look with coordinates")

print("\n Method 1: Basic iteration with coordinates")
for row_index in range(len(grid)):  #Loop through rows
    for col_index in range(len(grid[row_index])): #loops through colums
        value = grid[row_index][col_index]
        print(f"grid[{row_index}][{col_index}] = '{value}'")
        
#Method 2: Using enumerate() for cleaner code
print("\n Method 2: Using enumerate()")
for row_index, row in enumerate (grid):
    for col_index, value in enumerate(row):
        print(f" Position ({row_index},{col_index}: '{value}')")
        
#Method 3: Practical example - game board
print("\nMethod 3: Tic-tac-toe board example")
game_board = [["X","O"," "],[" ","X","O"],["O"," ","X"]]

print("Current board state:")
for row_index, row in enumerate(game_board):
    print("  " + " | ".join(row))  # Join elements with " | "
    if row_index < len(game_board) - 1:
        print("  " + "-" * 9)  # Horizontal separator
        
# Find empty positions
print("\nEmpty positions (available moves):")
for row_index, row in enumerate(game_board):
    for col_index, value in enumerate(row):
        if value == " ":
            print(f"  Position ({row_index},{col_index}) is empty")
            
# Method 4: Real-world example - Temperature grid
print("\nMethod 4: Temperature monitoring system")
temperatures = [
    [22, 23, 21, 20],  # Monday temperatures (4 readings)
    [24, 25, 23, 22],  # Tuesday
    [20, 19, 21, 22]   # Wednesday
]
days = ["Monday", "Tuesday", "Wednesday"]
times = ["Morning", "Noon", "Evening", "Night"]     

print("Weekly temperature readings:")
for day_index, day_temps in enumerate(temperatures):
    print(f"\n{days[day_index]}:")
    for time_index, temp in enumerate(day_temps):
        print(f"  {times[time_index]}: {temp}°C")
        