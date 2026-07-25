
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        if len(nums) > 1:
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i!=j and nums[i] + nums[j] == target:
                        result.append(i)
                        result.append(j)
                        return result
                    

