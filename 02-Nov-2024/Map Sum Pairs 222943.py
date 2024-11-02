# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class MapSum:

    def __init__(self):
        self.root = {}

    def insert(self, key: str, val: int) -> None:
        tmp = self.root
        for ch in key:
            if ch not in tmp:
                tmp[ch] = {}
            tmp = tmp[ch]
        tmp['#'] = val

    def sum(self, prefix: str) -> int:
        tmp = self.root
        for ch in prefix:
            if ch not in tmp:
                return 0
            tmp = tmp[ch]
        # use dfs to get the sum of all the leaves that have this prefix
        def dfs(src_node):
            sum_ = 0
            stack_ = []
            stack_.insert(0, src_node)

            while len(stack_):
                src_node = stack_.pop(0)
                keys = list(src_node.keys())
                for k in keys:
                    if '#' == k:
                        sum_ += src_node[k]
                    else:
                        stack_.insert(0, src_node[k])

            return sum_
        answer = dfs(tmp)

        return answer        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)