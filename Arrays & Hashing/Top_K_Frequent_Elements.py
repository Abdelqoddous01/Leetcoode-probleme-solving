class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top={}

        for i in nums:
            if(i not in top):
                top[i]=nums.count(i)

        top= dict(sorted(top.items(), key=lambda item: item[1],reverse=True))
        results=list(top)[0:k]

        return results