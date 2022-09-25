import collections

def minWindow(s, t):
    i = 0
    res = float('inf'), None, None
    count_t = collections.Counter(t)
    count_window = collections.defaultdict()
    formed = 0

    for j in range(len(s)):
        ch = s[j]

        count_window[ch] = count_window.get(ch, 0) + 1

        if ch in count_t and count_window[ch]==count_t[ch]: 
            formed += 1

        
        while formed==len(count_t) and i<=j:
                
            if j-i+1 < res[0]:
                res = (j-i+1, i, j)
            
            ch = s[i]
            count_window[ch]-=1

            if ch in count_t and count_window[ch]<count_t[ch]:
                formed -= 1

            i+=1
    
    min_len , l, r = res

    if min_len==float('inf'):
            return ""
    return s[l:r+1]


s = "ADOBECODEBANC"
t = "ABC"
print("Min len = ", minWindow(s, t))