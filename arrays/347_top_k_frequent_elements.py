class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        count  = {}
        for x in nums:
            count[x] = count.get(x,0) + 1
        ranked = sorted(count, key = count.get, reverse = True)
        return ranked[:k]
        