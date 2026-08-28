class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        p = []
        nums.sort()

        for i in range(len(nums)):
            s = set()

            for j in range(i + 1, len(nums)):
                k = -(nums[i] + nums[j])

                if k in s:
                    x = [nums[i], nums[j], k]
                    x.sort()
                    if x not in p:
                        p.append(x)

                s.add(nums[j])

        return p
