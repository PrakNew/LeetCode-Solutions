"""
Idea: Sets

Time complexity : O(n)
Space complexity: O(n)
"""

class Solution:
    def numUniqueEmails(self, emails):
        
        def validate(mail):
            mail_id = ""
            local_name, domain_name = mail.split('@')
            for ch in local_name:
                if ch == '+':
                    break
                elif ch != '.':
                    mail_id += ch

            return mail_id + '@' + domain_name
        
        seen = set()
        
        for email in emails:
            mail_id = validate(email)
            seen.add(mail_id)
        
        return len(seen)
        