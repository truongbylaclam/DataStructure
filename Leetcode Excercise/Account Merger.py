# Depth First Search
# This is the basic algorithm to explore the graph

# Dict is not interable so we import a defaultdict, which is an external dict provided
# by Python to iterate through the list
from collections import defaultdict

accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

def accountsMerge(A):
        G, seen, ans = defaultdict(list), set(), []

        for acc in A:
            for i in range(2,len(acc)):
                G[acc[i]].append(acc[i-1])
                G[acc[i-1]].append(acc[i])

        def dfs(email):
            seen.add(email)
            emailList = [email]
            for E in G[email]:
                if E not in seen:
                    emailList.extend(dfs(E))
            return emailList
        for acc in A:
            if acc[1] not in seen:
                ans.append([acc[0]] + sorted(dfs(acc[1])))
        return ans

print(accountsMerge(accounts))