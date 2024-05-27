l = [1, 2, 3, 4]
n = len(l)


def check(curr, n, arr, arr1):
    if curr == n:
        arr1.append(arr)
        return

    arr.append(l[curr])
    check(curr + 1, n, list(arr), arr1)
    arr.pop()

    check(curr + 1, n, list(arr), arr1)


arr1 = []
check(0, n, [], arr1)

print(arr1) #This will give all the combinations of l
