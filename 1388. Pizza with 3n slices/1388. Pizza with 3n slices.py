'''
Problem can be reframed as follows: Given a circular array of 3n elements, choose the maximum
sum subsequence with n elements.     

Since array is circular, element 1 and n cannot coexists in same subsequence. 

Time complexity : O(mn)
Space complexity: O(mn)

'''

def maximumSumSubsequence(A):

    n = len(A)//3 

    if n==0:
            return 0
        
    if 1<=len(A)<=3:
        return max(A)

    def util(A, i, ct, n):
        
        if ct>=n:
            return 0

        if i>=len(A):
            return 0 
        
        key = str(i) + '|' + str(ct)

        if key not in lookup:

            # include current item to subsequence, recur from i+2
            # print(A[i], ct)
            include = A[i] + util(A, i+2, ct+1, n) 

            # exclude current item from subsequence, recur from i+1
            exclude = util(A, i+1, ct, n) 

            lookup[key] = max(include, exclude)
        
        # print(key, lookup[key])
        return lookup[key]


    lookup = {}

    # include first slice
    first_slice = util(A[:-1], 0, 0, n)

    lookup = {}

    # include last slice
    last_slice = util(A[1:], 0, 0, n)

    # print(first_slice)
    # print(last_slice)

    return max(first_slice, last_slice)
    # return 0

if __name__ == '__main__':

    arr = [1,2,3,4,5,6]

    print("Answer = ", maximumSumSubsequence(arr))