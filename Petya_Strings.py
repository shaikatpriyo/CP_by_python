
s = input().strip()


numbers = s.split('+')


numbers.sort()


result = '+'.join(numbers)


print(result)