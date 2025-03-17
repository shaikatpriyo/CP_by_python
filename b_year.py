def has_distinct_digits(year):
    return len(set(str(year))) == len(str(year))


def next_distinct_year(y):
    y += 1
    while not has_distinct_digits(y):
        y += 1
    return y


y = int(input())
print(next_distinct_year(y))
