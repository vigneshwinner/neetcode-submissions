class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, 1
        while l < len(numbers) and r < len(numbers):
            while r < len(numbers) and numbers[l] < numbers[r]:
                if numbers[l] + numbers[r] == target:
                    return [numbers[l], numbers[r]]
                r += 1
            l += 1