"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""
import collections

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count_dict = collections.defaultdict(int)
        for num in nums:
            count_dict[num] += 1

        return map(lambda x: x[0], reversed(sorted([(n, c) for n, c in count_dict.items()], key=lambda x: x[1])))[:k]



s = Solution()

print(s.topKFrequent([1,1,1,2,2,3], 2))

print s.topKFrequent([1], 1)


print [1, 2, 3][:2]