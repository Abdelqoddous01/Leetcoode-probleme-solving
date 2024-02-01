class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupes=[]
        dic={}
        for word in strs:
            so="".join(sorted(word))
            if so not in dic:
                dic[so]=[word]
            else:
                dic[so].append(word)
                
        for key in dic:
            groupes.append(dic[key])
        
        return groupes  
