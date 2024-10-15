from sortedcontainers import SortedList
class MyCalendarTwo:

    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        stuple, etuple = (start, 1), (end, -1)
        self.calendar.add(stuple)
        self.calendar.add(etuple)
        total = 0
        for _, count in self.calendar:
            total += count
            if total == 3:
                self.calendar.remove(stuple)
                self.calendar.remove(etuple)
                return False
        return True
        
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)