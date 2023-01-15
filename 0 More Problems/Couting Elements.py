def countElements(arr):
    res = 0
    mp = {}
    
    for num in arr:
        if num+1 in arr:
            res += 1
            mp[num] = []
        if num+1 in arr and arr.index(num+1) not in mp[num]:
            mp[num].append(arr.index(num+1))
    
    return res