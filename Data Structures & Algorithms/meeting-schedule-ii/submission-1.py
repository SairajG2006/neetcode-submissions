"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        mp = defaultdict(int)
        for interval in intervals:
            mp[interval.start] += 1
            mp[interval.end] -= 1
        
        maxRooms = 0
        active = 0
        for i in sorted(mp):
            active += mp[i]
            maxRooms = max(maxRooms, active)
        
        return maxRooms
            
            
        