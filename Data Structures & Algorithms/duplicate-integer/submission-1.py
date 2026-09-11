
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for numb in nums:
            if numb in seen:
                return True
            seen.add(numb)
        return False


       
        