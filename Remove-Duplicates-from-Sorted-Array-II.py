1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        """
4        elements should be returned at most twice 
5        element > 0 ----> add to list
6        element > 1 ----> add to list
7        element > 2 ----> add to list
8        element > 3 ----> Skip
9        Key :seen elements , value return number of occurances 
10        """
11        result=[]
12        seen={}
13        for i in nums:
14            if seen.get(i,0)<2:
15                result.append(i)
16                seen[i] = seen.get(i, 0) + 1  #Add 1 occurrence” and update count 
17                """
18                seen.get(1,0)  --->ncrease the count of x in the dictionary by 1,If x doesn’t exist yet, start from 0
19                1>> seen
20                {1:1}
21                increase the count 
22                
23                """
24        nums[:] = result 
25        return len(result)
26        
27       