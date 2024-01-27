class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len1=len(s)
        len2=len(t)
        dict1={}
        
        if len1!=len2:
            return False
        
        for char in s:
            if char not in dict1:
                dict1[char]=s.count(char)
                
        for char in t:
            if char not in dict1 or t.count(char)!=dict1[char]:
                return False
        return True