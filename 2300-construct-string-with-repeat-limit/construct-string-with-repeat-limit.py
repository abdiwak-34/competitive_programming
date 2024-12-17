from heapq import heapify, heappop, heappush
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        max_heap = []
        for char, count in freq.items():
            heappush(max_heap, (-ord(char), count))
        
        result = []
        
        while max_heap:
            ascii_val, count = heappop(max_heap)
            char = chr(-ascii_val)
            use_count = min(count, repeatLimit)
            result.append(char * use_count)
            count -= use_count
            
            if count > 0:
                if not max_heap:
                    break
                
                next_ascii_val, next_count = heappop(max_heap)
                next_char = chr(-next_ascii_val)
                result.append(next_char)
                next_count -= 1
                
                if next_count > 0:
                    heappush(max_heap, (next_ascii_val, next_count))
                
                heappush(max_heap, (ascii_val, count))
        
        return ''.join(result)
