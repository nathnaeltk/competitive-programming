class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged = ""
        for ch in address:
            if ch == ".":
                defanged += "[.]"
            else: 
                defanged += ch
        return defanged
                