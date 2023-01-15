# Reorganize the string so that resultant string has no two same adjacent characters
# Sorting by count concept is used

def reorganize(s):
    A = []
    n = len(s)
    for count, ch in sorted((s.count(ch), ch) for ch in set(s)):
        if count > (n+1)/2: # cannot shard the string
            return "" 
        A.extend(ch * count)
    ans = [None] * n
    ans[::2], ans[1::2] = A[n//2:], A[:n//2]

    return ''.join(ans)

if __name__ == '__main__':
    s = "aaabb"
    print("Reorganized string: ", reorganize(s))