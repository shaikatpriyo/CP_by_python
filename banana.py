k, n, w = map(int, input().split())
total_cost = k * w * (w + 1) // 2
amount_to_borrow = max(0, total_cost - n)
print(amount_to_borrow)