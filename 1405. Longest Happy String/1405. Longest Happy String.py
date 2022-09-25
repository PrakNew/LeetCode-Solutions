from heapq import heappush, heappop


def longestDiverseString(self, a, b, c):
    
    heap = []
    
    if a>0:
        heappush(heap, (-a, 'a'))
    if b>0:
        heappush(heap, (-b, 'b'))
    if c>0:
        heappush(heap, (-c, 'c'))
    
    res = ''
    
    while heap:
        freq1, char1 = heappop(heap)
        
        if len(res)>=2 and res[-1]==char1 and res[-2]==char1: # if last two characters are same
            # check if heap is not empty
            if len(heap)==0:
                return res
            
            # append char2 to string
            freq2, char2 = heappop(heap)
            res += char2
            freq2 += 1
            if freq2!=0:
                heappush(heap, (freq2, char2))
            
            # char1 is not used push it back
            heappush(heap, (freq1, char1))
        else:
            # append char1 into string
            res += char1
            freq1 += 1
            if freq1!=0:
                heappush(heap, (freq1, char1))

    return res