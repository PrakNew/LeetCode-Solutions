class Solution:
    def twoCitySchedCost(self, costs):
        # send every person to city A
        res = 0
        for i in range(len(costs)):
            res += costs[i][0]
        refund = [0] * len(costs)
        # refund you get when you send everyone to city B
        for i in range(len(costs)):
            refund[i] = costs[i][1] - costs[i][0]
        refund.sort() # Sort refund and choose first n cities -> maximize refund
        for i in range(len(costs)//2):
            res += refund[i]
        return res