class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        counter=[]
        index=0

        if len(nums)!=0:
            counter=[1]*len(nums)
        else:
            counter=[0]

        for i in range(1,len(nums)):
            if nums[i-1]+1==nums[i]:
                counter[index]+=1
            elif nums[i-1]==nums[i]:
                continue
            else:
                index+=1
                

        return max(counter)