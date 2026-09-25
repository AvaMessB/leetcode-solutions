class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        while(len(nums) > 1 and i+1 < len(nums)):
            if (nums[i] == nums[i+1]):
                nums.remove(nums[i])
                i -= 1
            i += 1 
        return len(nums)
##########################################################

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow = 0
        fast = 1
        while slow < len(nums) and fast < len(nums):
            if(nums[slow] != nums[fast]):
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
            else:
                fast += 1 
        return slow+1



        