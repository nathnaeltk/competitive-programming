# Problem: Reorganize String - https://leetcode.com/problems/reorganize-string/description/

import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        max_heap = [(-value, key) for key, value in freq.items()]
        heapq.heapify(max_heap)
        
        if any(-count > (len(s) + 1) // 2 for count, char in max_heap):
            return ""
        
        result = []
        prev_freq, prev_char = 0, ''
        
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char)
            
            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))
            
            prev_freq, prev_char = freq + 1, char
        
        return ''.join(result)