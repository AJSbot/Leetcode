class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {c: s.count(c) for c in set(s)}
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1
