import collections

class Solution:
    def leastInterval(self, tasks, n):
        frequencies = [0] * 26
        for task in tasks:
            frequencies[ord(task)-ord('A')] += 1
            
        frequencies.sort()
        f_max = frequencies.pop()
        idle_slots = (f_max - 1) * n
        
        while frequencies and idle_slots > 0:
            idle_slots -= min(f_max-1, frequencies.pop())
            
        idle_slots = max(0, idle_slots)
        return idle_slots + len(tasks)
        
        