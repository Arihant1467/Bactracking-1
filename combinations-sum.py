'''
Time Complexity : 0(n*n)
Space Complexity : 0(n)
Did it run on leet code : Yes
Challenges faced: How to backtrack path and what should be the root
​
Algorithm
​
1. Start with an empty root
2. Add a num in the path and then recursively pick the next num in array and check whether the sum is more or less,
if its less then pick next number, if it is greater, ignore. If its equal, add the path in the result
​
​
​
'''
class Solution(object):
    
    def __init__(self):
        self.result =[]
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        path = []
        self.helper(candidates,path,target,0)
        return self.result
    
    def helper(self,candidates,path,target,i):
        
        if target==0:
            self.result.append(path[::])
            return
        
        for k in range(i,len(candidates)):
            
            if candidates[k]>target:
                break
            
            path.append(candidates[k])
            self.helper(candidates,path,target-candidates[k],k)
            path.pop()