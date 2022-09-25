def productExceptSelf(nums):
    n = len(nums)
    prefix = nums[:]
    postfix = nums[:]
    
    for i in range(1, n):
        prefix[i] *= prefix[i-1]
        postfix[n-i-1] *= postfix[n-i]
    
    output = []
    
    for i in range(n):
        if i==0:
            output.append(postfix[i+1])
        elif i==n-1:
            output.append(prefix[i-1])
        else:
            output.append(prefix[i-1] * postfix[i+1])
    
    return output