# Using LRU cache
from functools import lru_cache

inputs = input("Enter steps and array length : ").split()
steps, arrLen = int(inputs[0]), int(inputs[1])

mod = 10**9 + 7

@lru_cache(None) 
def calculate1(pos, steps):

    if pos<0 or pos>=arrLen: # consider only valid array positions
        return 0
    if pos > steps:         # not a step
        return 0
    if pos==steps:       # valid step
        return 1
    steps -= 1          # have taken a valid step

    # possible steps are: 1.right 2.left 3.stay
    return (calculate1(pos+1, steps) + calculate1(pos-1, steps) + calculate1(pos, steps)) % mod

# Using hashmaps to recall already computed results
mp = {}
def calculate2(pos, steps):
    if pos<0 or pos>=arrLen: # consider only valid array positions
        return 0
    if pos > steps:         # not a step
        return 0
    if pos==steps:       # valid step
        return 1
    steps -= 1          # have taken a valid step

    if (pos+1, steps) not in mp:
        mp[(pos+1, steps)] = calculate2(pos+1, steps)
    if (pos-1, steps) not in mp:
        mp[(pos-1, steps)] = calculate2(pos-1, steps)
    if (pos, steps) not in mp:
        mp[(pos, steps)] = calculate2(pos, steps)

    # possible steps are: 1.right 2.left 3.stay
    return (mp[(pos+1, steps)] + mp[(pos-1, steps)] + mp[(pos, steps)]) % mod

print("Output using LRU cache ", calculate1(0, steps))
print("Output using hashmap ", calculate2(0, steps))