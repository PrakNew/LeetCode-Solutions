import collections, random, heapq

class Solution:
    def topKFrequent(self, A, k):
        
        def heapSort():
            if k==len(A):
                return A
            count = collections.Counter(A)
            return heapq.nlargest(k, count, key = count.get)
        
        def quickSelection():
            count = collections.Counter(A)
            unique = list(count.keys())

            def partition(left, right, pivot_index):
                pivot_frequency = count[unique[pivot_index]]
                unique[right], unique[pivot_index] = unique[pivot_index], unique[right]
                store_index = left
                for i in range(left, right):
                    if count[unique[i]] < pivot_frequency:
                        unique[i], unique[store_index] = unique[store_index], unique[i]
                        store_index += 1

                unique[store_index], unique[right] = unique[right], unique[store_index]

                return store_index

            def quickSelect(left, right, k_smallest):
                if left == right:
                    return 
                pivot_index = random.randint(left, right)
                pivot_index = partition(left, right, pivot_index)
                if k_smallest == pivot_index:
                    return
                elif k_smallest < pivot_index:
                    quickSelect(left, pivot_index-1, k_smallest)
                else:
                    quickSelect(pivot_index+1, right, k_smallest)


            n = len(unique)
            quickSelect(0, n-1, n-k)
            return unique[n-k:]
        
        return quickSelection()
        return heapSort()
        