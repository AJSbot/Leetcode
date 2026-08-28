class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a= str(x)
        rev=a[::-1]
        if a==rev:
            return bool(1)
        else:
            return bool(0)
            
