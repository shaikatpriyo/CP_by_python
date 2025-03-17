s = input().strip()
lower_count = sum(1 for char in s if char.islower())
upper_count = sum(1 for char in s if char.isupper())

if upper_count > lower_count:
    print(s.upper())
else:
    print(s.lower())