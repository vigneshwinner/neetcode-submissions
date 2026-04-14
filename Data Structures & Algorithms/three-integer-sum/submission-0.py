class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        n = len(nums)
        for i in range(n):
            l, r = i + 1, n - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                    continue
                else:
                    r -= 1
                    continue
                l, r = l + 1, r - 1
        return [list(i) for i in res]           