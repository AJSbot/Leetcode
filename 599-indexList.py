class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        ans=[]
        p=10000
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                   s=i+j
                   if s<p:
                    p=s
                    ans=[list1[i]]                 
                   elif s==p:
                    ans.append(list1[i])
        return ans 


            
        
