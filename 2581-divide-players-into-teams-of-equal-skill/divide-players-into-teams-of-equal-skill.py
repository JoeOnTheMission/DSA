class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        number_of_teams = n // 2
        total = sum(skill)
        
        if total % number_of_teams != 0:
            return -1
        
        target = total // number_of_teams
        skill.sort()
        
        chemistry = 0
        i, j = 0, n - 1
        
        while i < j:
            if skill[i] + skill[j] != target:
                return -1
            chemistry += skill[i] * skill[j]
            i += 1
            j -= 1
        
        return chemistry
