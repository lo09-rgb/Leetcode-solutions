class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        n = len(nums)

        for start in range(n):
            running_sum = 0

            for end in range(start, n):
                running_sum += nums[end]

                if running_sum == k:
                    count += 1

        return count
