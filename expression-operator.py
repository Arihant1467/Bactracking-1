class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        
        if not num:
            return []
        
        self.result = []
        self.helper(1,int(num[0]),num[0]+"",num,target)
        return self.result
        
    def helper(self,startPosition,currentValue,currentPath,num,target):
        
       
        if startPosition==len(num) and currentValue==target:
            self.result.append(currentPath)
            return
        
        elif startPosition<len(num):
            intValue = int(num[startPosition])
            self.helper(startPosition+1,currentValue+intValue,currentPath+"+"+num[startPosition],num,target)
            self.helper(startPosition+1,currentValue-intValue,currentPath+"-"+num[startPosition],num,target)
            y=(int(num[startPosition-1])*intValue)+(currentValue-int(num[startPosition-1]))
            self.helper(startPosition+1,y,currentPath+"*"+num[startPosition],num,target)
            
        else:
            return
        
        return