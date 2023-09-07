from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numbersSet = set()

        for i in nums:
            if i in numbersSet:
                return True
            numbersSet.add(i)
        return False
