class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        sortedSpells = [(spell,index) for index, spell in enumerate(spells)]
        sortedSpells.sort()
        potions.sort()
        
        answer = [0] * len(spells)
        potionCnt = len(potions)
        pid = potionCnt - 1
        for spell,index in sortedSpells:
            while pid >= 0 and (spell * potions[pid]) >= success:
                pid -= 1
            answer[index] = potionCnt - (pid +1)
        return answer