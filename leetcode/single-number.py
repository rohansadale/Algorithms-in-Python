class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return -1
            
        num = nums[0]
        for i in range(1, len(nums)):
            num ^= nums[i]
        return num