class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = {}
        losses = {}

        # Count wins and losses for each player
        for winner, loser in matches:
            wins[winner] = wins.get(winner, 0) + 1
            losses[loser] = losses.get(loser, 0) + 1

        # Identify players who have not lost any matches
        not_lost_any = [player for player, win_count in wins.items() if win_count > 0 and player not in losses]

        # Identify players who have lost exactly one match
        lost_once = [player for player, loss_count in losses.items() if loss_count == 1]

        return [sorted(not_lost_any), sorted(lost_once)]