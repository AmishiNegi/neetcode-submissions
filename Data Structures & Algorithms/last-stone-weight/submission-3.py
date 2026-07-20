class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            first = max(stones)
            stones.remove(first)
            second = max(stones)
            stones.remove(second)

            if first > second:
                stones.append(first - second)
            elif first < second:
                stones.append(second - first)
        if len(stones) == 1: 
            return stones[0]
        else:
            return 0
        