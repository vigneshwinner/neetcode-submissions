class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = list(magazine)
        for r in ransomNote:
            if r not in mag:
                return False
            mag.remove(r)
        return True