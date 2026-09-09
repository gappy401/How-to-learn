class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict ={num:idx for idx, num in enumerate(nums)}
        for i in range(len(nums)):
            curr_id=i
            look_for=target-nums[i]
            if (look_for in my_dict) & (my_dict.get(look_for)!=i):
                return [i,my_dict.get(look_for)]
        



        