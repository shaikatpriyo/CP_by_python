def can_binary_hear(T, frequencies):
    min_freq = 67
    max_freq = 45000
    
    for X in frequencies:
        if min_freq <= X <= max_freq:
            print("YES")
        else:
            print("NO")

# Read number of test cases
T = int(input())
frequencies = [int(input()) for _ in range(T)]

# Check if Binary can hear the frequencies
can_binary_hear(T, frequencies)
