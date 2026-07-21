print("\n=== 2D LIST ITERATION ===")

# Create a sample 2D list (3x3 grid)
grid = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"]
]

# Method 1: Basic nested loop with coordinates
print("\nMethod 1: Basic iteration with coordinates")
for row_index in range(len(grid)):           # Loop through rows
    for col_index in range(len(grid[row_index])):  # Loop through columns
        value = grid[row_index][col_index]
        print(f"  grid[{row_index}][{col_index}] = '{value}'")

# Method 2: Using enumerate() for cleaner code
print("\nMethod 2: Using enumerate()")
for row_index, row in enumerate(grid):        # enumerate gives (index, value)
    for col_index, value in enumerate(row):   # enumerate again for columns
        print(f"  Position ({row_index},{col_index}): '{value}'")

# Method 3: Practical example - Game board
print("\nMethod 3: Tic-Tac-Toe board example")
game_board = [
    ["X", "O", " "],
    [" ", "X", "O"],
    ["O", " ", "X"]
]

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