class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)

        s1_count = {}
        s2_count = {}

        for i in range(len(s1)):
            s1_count[s1[i]] = 1 + s1_count.get(s1[i], 0)
        
        for i in range(len(s2) - len(s1) + 1):
            for chara in s2[l+i:r+i]:
                s2_count[chara] = 1 + s2_count.get(chara, 0)
            if s2_count == s1_count:
                return True
            s2_count.clear()
        return False
        