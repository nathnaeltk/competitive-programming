#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        check_set = set(a)
        
        #code here
        for i in b:
            if i in check_set:
                continue
            check_set.add(i)
        return len(check_set)
            

