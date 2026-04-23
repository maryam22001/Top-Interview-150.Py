1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        """
4       
5========================
6PYTHON LIST vs SET vs SORT
7========================
8
91) sorted() vs sort()
10
11- sorted(x)
12    • Works on ANY iterable (list, set, tuple, etc.)
13    • Returns a NEW sorted list
14    • Does NOT modify original data
15
16    Example:
17        new_list = sorted(nums)
18
19- list.sort()
20    • Works ONLY on lists
21    • Modifies list in-place
22    • Returns None
23
24    Example:
25        nums.sort()
26
27
28========================
292) LIST METHODS
30========================
31
32- nums.append(x)     → add element at end
33- nums.pop()         → remove last element
34- nums.pop(i)        → remove element at index i
35- nums.remove(x)     → remove first occurrence of value x
36- nums.insert(i, x)  → insert x at index i
37- nums.sort()        → sort list in-place
38- nums.reverse()     → reverse list
39- nums.count(x)      → count occurrences of x
40- nums.index(x)      → first index of x
41
42
43========================
443) SET METHODS
45========================
46
47- s.add(x)           → add element
48- s.remove(x)        → remove element (ERROR if not found)
49- s.discard(x)       → remove element safely (no error)
50- s.pop()            → remove random element
51- s.clear()          → remove all elements
52
53SET OPERATIONS:
54- a | b              → union
55- a & b              → intersection
56- a - b              → difference
57
58
59========================
604) KEY DIFFERENCES
61========================
62
63LIST:
64- Ordered
65- Allows duplicates
66- Supports indexing
67
68SET:
69- Unordered
70- No duplicates
71- No indexing
72- Fast lookup (O(1))
73
74========================
755) QUICK MEMORY RULE
76========================
77
78- sorted() → returns NEW sorted list
79- sort()   → sorts original list
80- list     → ordered + duplicates allowed
81- set      → unique + unordered
82
83        """
84        seen = set()
85        result = []
86
87        for x in nums:
88            if x not in seen:
89                result.append(x)
90                seen.add(x)
91
92        nums[:] = result
93        return len(result)