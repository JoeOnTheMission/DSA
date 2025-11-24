class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = {}
        lose = {}
        soln = [[],[]]
        for match in matches:
            # win update
            win[match[0]] = win.get(match[0], 0) + 1
            # lose update
            lose[match[1]] = lose.get(match[1],0) + 1
        for winner in win:
            if winner not in lose:
                soln[0].append(winner)
        for loser in lose:
            if lose[loser] == 1:
                soln[1].append(loser)
        soln[0].sort()
        soln[1].sort()
        return soln