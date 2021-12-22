 # Account Merge for the Leetcode Challenge on November 29th 2021

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ## Using DFS to find connected component
        hashMap = {}
        for i in range(0, len(accounts)):
            for j in range(1, len(accounts[i])):
                if hashMap[i][j] not in hashMap:
                    hashMap[accounts[i][0]] = accounts[i][j]

            