class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=list(s)
        v="aeiouAEIOU"
        x = [c for c in a if c in v]
        x.reverse()
        j=0
        for i  in range(len(a)):
            if a[i] in v:
                a[i]=x[j]
                j+=1
        return "".join(a)

