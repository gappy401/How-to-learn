class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=0

        if not nums:
            return j
        

        for i in range(len(nums)):
            if nums[i]!=val:
                nums[j]=nums[i]
                j+=1
            
        return j

        