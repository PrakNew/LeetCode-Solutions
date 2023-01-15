

def find(N):
    next_mul3 = 3
    next_mul5 = 5
    i3 = 0
    i5 = 0
    ugly = [1]

    for i in range(1, N):
        next_ugly = min(next_mul3, next_mul5)

        ugly.append(next_ugly)

        if next_ugly==next_mul3:
            i3+=1
            next_mul3 = ugly[i3]*3
        
        if next_ugly==next_mul5:
            i5+=1
            next_mul5 = ugly[i5]*5

    print(next_ugly)


if __name__ == '__main__':
    
    find(8)
