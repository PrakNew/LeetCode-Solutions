import collections

class Solution:
    def accountsMerge(self, accounts):
        
        graph = collections.defaultdict(set)
        email_name = {}
        
        for i in range(len(accounts)):
            name, mails = accounts[i][0], accounts[i][1:]
            for mail in mails:
                graph[mail].add(mails[0])
                graph[mails[0]].add(mail)
                email_name[mail] = name
        
        res = []
        visited = set()
        for email in graph:
            if email not in visited:
                stack = set([email])
                mail_group = set()
                while stack:
                    temp = set()
                    for node in stack:
                        mail_group.add(node)
                        visited.add(node)
                        for nei in graph[node]:
                            if nei not in visited:
                                temp.add(nei)
                    stack = temp
                contact = [email_name[email]]
                for mail in sorted(mail_group):
                    contact += mail,
                res += contact,
        
        return res
                