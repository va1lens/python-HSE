"""
https://leetcode.com/problems/number-of-boomerangs/description/
?envType=problem-list-v2&envId=hash-table
"""

from collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        count_boomerangs: int = 0
        for p1 in points:
            distances: defaultdict[int] = defaultdict(int)
            for p2 in points:
                if p1 == p2:
                    continue
                dist: int = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
                distances[dist] += 1
            for dist in distances.values():
                count_boomerangs += dist * (dist - 1)
        return count_boomerangs
