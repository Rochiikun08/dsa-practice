class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = {}
        for x in nums:
            count[x] = count.get(x,0) + 1
        for ch in count:
            if count[ch] == 1:
                return ch
        