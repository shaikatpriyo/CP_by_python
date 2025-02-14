# Read the number of statements
n = int(input())

# Initialize x to 0
x = 0

# Process each statement
for _ in range(n):
    statement = input()
    if "++" in statement:
        x += 1
    elif "--" in statement:
        x -= 1

# Output the final value of x
print(x)