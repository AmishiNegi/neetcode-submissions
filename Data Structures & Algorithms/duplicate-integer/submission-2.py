class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        encountered = set()
        for i in range(len(nums)):
            if nums[i] not in encountered:
                encountered.add(nums[i])
            else:
                return True

        return False