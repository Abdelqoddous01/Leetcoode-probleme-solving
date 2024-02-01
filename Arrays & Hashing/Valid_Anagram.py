class Solution:
    def isAnagram(s: str, t: str) -> bool:
        for i in set(s+t):
            if s.count(i)!=t.count(i):
                return False
        
        return True
        
