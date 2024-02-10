class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        string_map = {}
        for i, string in enumerate(list1):
            if string in list2:
                string_map[string] = i + list2.index(string)
                
        minimum_reps = min(string_map.values())
        common_with_least_index_sum = [string for string in string_map if string_map[string] == minimum_reps]
        
        return common_with_least_index_sum