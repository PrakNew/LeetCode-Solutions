# first (n-1)! numbers start with 1, next (n-1)! numbers start with 2 and so on
import math

def permutationSequence(n, k):
    numbers = list(range(1, n+1))
    permutation = ''
    k-=1
    print(numbers)
    while n>0:
        n-=1
        # print(n)
        index, k = divmod(k, math.factorial(n))
        permutation += str(numbers[index])
        # remove used number
        numbers.remove(numbers[index])
        # print(numbers)
    
    return permutation

if __name__ =='__main__':
    n = 3
    k = 3
    print("Ans : ", permutationSequence(n, k))