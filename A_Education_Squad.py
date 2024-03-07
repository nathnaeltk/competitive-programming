

board = [input() for _ in range(3)]
# Count the number of individual heads who can claim victory
individual_victories = 0
for i in range(26):
    head = chr(ord('A') + i)
    if any(all(cell == head for cell in row) for row in board) or \
       any(all(board[j][i] == head for j in range(3)) for i in range(3)) or \
       all(board[i][i] == head for i in range(3)) or \
       all(board[i][2-i] == head for i in range(3)):
        individual_victories += 1

# Count the number of two-head teams that can claim victory
team_victories = 0
for i in range(26):
    for j in range(i+1, 26):
        head1 = chr(ord('A') + i)
        head2 = chr(ord('A') + j)
        if any(all(cell in (head1, head2) for cell in row) for row in board) or \
           any(all(board[k][l] in (head1, head2) for l in range(3)) for k in range(3)) or \
           all(board[k][k] in (head1, head2) for k in range(3)) or \
           all(board[k][2-k] in (head1, head2) for k in range(3)):
            team_victories += 1

print(individual_victories)
print(team_victories)
