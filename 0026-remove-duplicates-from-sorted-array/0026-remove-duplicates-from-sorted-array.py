class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 1 #holds index of next open spot
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]: #i is ahead in the loop
                nums[res] = nums[i]
                res += 1
        return res