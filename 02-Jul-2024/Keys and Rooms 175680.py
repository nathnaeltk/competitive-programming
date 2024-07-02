# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        lis=[]
        lis.extend(rooms[0])
        for i in lis:
            for j in rooms[i]:
                if(j not in lis):
                    lis.append(j)
        for i in range(1,len(rooms)):
            if(i not in lis):
                return(False)
        return(True)