def getKth(self, lo: int, hi: int, k: int) -> int:
    
    #  power of any number = power to convert it to 2^k + k
    
    def power(x):
        ct = 0
        while True:
            if x&1==0:
                # check if it is of form 2^k
                for i in range(33):
                    if x==1<<i:
                        return i+ct
                x/=2
            else:
                x = 3*x+1
            ct+=1
            x = int(x)
            # print(x)
        
    power_array = []
    
    for num in range(lo, hi+1):
        n = num
        p = power(num)
        power_array.append([p, n])
    
    power_array.sort()
    
    return power_array[k-1][1]