class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = []
        d = {')':'(', ']':'[', '}':'{'}

        for i in s:
            if i in "([{":
                a.append(i)
            elif not a or a.pop() != d[i]:
                return False

        return not a
