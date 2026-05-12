class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countM = Counter(magazine)
        countR = Counter(ransomNote)

        for c in ransomNote:
            if countM[c] < countR[c]:
                return False

        return True