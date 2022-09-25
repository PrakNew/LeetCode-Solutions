class Solution:
    def peopleIndexes(self, favoriteCompanies):
        
        company_code = {}
        code_company = {}
        n = len(favoriteCompanies)
        ct = 0
        
        favoriteCodes = []
        
        for i in range(n):
            code = []
            for j in range(len(favoriteCompanies[i])):
                if favoriteCompanies[i][j] not in company_code:
                    company_code[favoriteCompanies[i][j]] = ct
                if ct not in code_company:
                    code_company[ct] = favoriteCompanies[i][j]
                    ct+=1
                code.append(company_code[favoriteCompanies[i][j]])
            favoriteCodes.append(code)
        
        ans = set()
        
        def isSubset(i, j):
            for x in favoriteCodes[i]:
                if x not in favoriteCodes[j]:
                    return False
            return True
        
        res = []
        
        for i in range(n):
            subset = False
            for j in range(n):
                if len(favoriteCodes[i])<len(favoriteCodes[j]) and isSubset(i, j):
                    subset = True
            if not subset:
                res.append(i)
        
        return res
        