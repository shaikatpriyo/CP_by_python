def find_winner(n, s):
    a_wins = s.count('A')
    d_wins = s.count('D')
    
    if a_wins > d_wins:
        print("Anton")
    elif d_wins > a_wins:
        print("Danik")
    else:
        print("Friendship")



n = int(input().strip())
s = input().strip()

find_winner(n, s)
