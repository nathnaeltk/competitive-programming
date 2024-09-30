# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(set)
        for acc in accounts:
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
        
        res = []
        visit = set()

        for acc in accounts:
            if acc[1] not in visit:
                name = acc[0]
                stack = [acc[1]]
                emails = []
                while stack:
                    node = stack.pop()
                    if node not in visit:
                        visit.add(node)
                        stack.extend(graph[node])
                        emails.append(node)

                res.append([name] + sorted(emails))
        return res