1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        
4        nums.sort()   # better than sorted()
5
6        i = 0
7
8        while i < len(nums):
9            if nums[i] == val:
10                nums.remove(val)
11                """
12                remove the first occuance of the element so we use while not a for loop
13                """
14            else:
15                i += 1
16
17        return len(nums)