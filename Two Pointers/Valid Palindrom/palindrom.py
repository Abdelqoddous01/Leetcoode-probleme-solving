class Solution:
    def isPalindrome(self,s: str) -> bool:
        news=""
        for i in s:
            if i.isalpha() or i.isdigit():
                news+=i.lower()
                
        reversedNews="".join(list(reversed(news)))
        
        if news==reversedNews.lower():
            return(True)
        
        return False




res=Solution.isPalindrome("A man, a plan, a canal: Panama")
print(res)