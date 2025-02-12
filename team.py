# Read the number of problems
n = int(input())

# Initialize a counter for the number of problems they will solve
count = 0

# Iterate through each problem
for _ in range(n):
    # Read the three integers for the current problem
    a, b, c = map(int, input().split())
    
    # Check if at least two of them are sure about the solution
    if a + b + c >= 2:
        count += 1

# Output the result
print(count)
