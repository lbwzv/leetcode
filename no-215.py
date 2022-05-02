class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        l = 0
        while l < k - 1:
            l += 1
        return(nums[l])
