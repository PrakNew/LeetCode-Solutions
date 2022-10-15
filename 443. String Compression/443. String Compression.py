# This is a easy example to convert the values into a string count like a brute force

class Solution:
    def compress(self, chars) -> int:
        c=1
        prev=chars[0]
        s=prev
        for x in range(1,len(chars)):
            if chars[x]==prev:
                c+=1
            else:
                if c!=1:
                    s+=str(c)
                c=1
                prev=chars[x]
                s+=prev
        if c!=1:
            s+=str(c)
        chars[:]=list(s)
        return len(s)