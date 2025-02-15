m, n, a=map(int, input().split())

flagstones_l=(m+a-1)//a
flagstones_w=(n+a-1)//a

Total_flagstones=flagstones_l*flagstones_w
print(Total_flagstones)

