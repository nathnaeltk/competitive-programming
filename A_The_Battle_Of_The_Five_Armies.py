# Read space-separated integers on a line
a, b, c, d, e = map(int, input().split())

m, n, o, p, q = map(int, input().split())

team1power = a*m + b*n + c*o

team2power = d*p + e*q

if team1power > team2power:
    print("WIN")
elif team1power < team2power:
    print("LOSE")
else:
    print("DRAW")
