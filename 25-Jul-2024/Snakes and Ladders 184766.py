# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board):
        length = len(board)
        board.reverse()

        def positionOf(number):
            r = (number - 1) // length
            c = (number - 1) % length
            if r % 2:
                c = length - 1 - c
            return r, c
        
        q = deque()
        q.append([1, 0])

        visited = set()
        visited.add(1)

        while q:
            square, moves = q.popleft()

            for i in range(1, 7):
                nextSquare = square + i
                if nextSquare > length * length:
                    continue
                r, c = positionOf(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                if nextSquare == length * length:
                    return moves + 1
                if nextSquare not in visited:
                    visited.add(nextSquare)
                    q.append([nextSquare, moves + 1])

        return -1