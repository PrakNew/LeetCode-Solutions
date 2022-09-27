# This is a pattern finding question done in O(N) time and space complexity

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        d=list(dominoes)
        l=len(dominoes)
        Left=['.']*(l+1)
        right=['.']*(l+1)
        for x in range(l):
            if d[x]=='R':
                right[x]='R1'
            elif d[x]=='L':
                right[x]='L'
            elif d[x]=='.':
                if right[x-1][0]=='R':
                    right[x]='R'+str(int(right[x-1][1:])+1)
        for x in range(l-1,-1,-1):
            if d[x]=='L':
                Left[x]='L1'
            elif d[x]=='R':
                Left[x]='R'
            elif d[x]=='.':
                if Left[x+1][0]=='L':
                    Left[x] = f'L{str(int(Left[x + 1][1:]) + 1)}'
        print(Left)
        print(right)
        final=['.']*l
        for x in range(l):
            if right[x]=='.' and Left[x]=='.':
                final[x]='.'
            elif right[x]=='.' and Left[x]!='.':
                final[x]='L'
            elif Left[x]=='.' and right[x]!='.':
                final[x]='R'
            elif Left[x]=='R':
                final[x]='R'
            elif right[x]=='L':
                final[x]='L'
            else:

                r1=right[x]
                l1=Left[x]
                if int(r1[1:])<int(l1[1:]):
                    final[x]='R'
                elif int(r1[1:])>int(l1[1:]):
                    final[x]='L'
                else:
                    final[x]='.'

        return ''.join(final)
        
        