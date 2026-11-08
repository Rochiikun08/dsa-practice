class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        total = 0
        for x in nums:
            total += x
            result.append(total)
        return result