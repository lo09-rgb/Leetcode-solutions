class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums)):

            # Skip duplicate fixed elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            target = -nums[i]

            while left < right:

                current_sum = nums[left] + nums[right]

                if current_sum == target:

                    result.append(
                        [nums[i], nums[left], nums[right]]
                    )

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while (
                        left < right
                        and nums[left] == nums[left - 1]
                    ):
                        left += 1

                    # Skip duplicate right values
                    while (
                        left < right
                        and nums[right] == nums[right + 1]
                    ):
                        right -= 1

                elif current_sum < target:
                    left += 1

                else:
                    right -= 1

        return result


# Example
nums = [-1, 0, 1, 2, -1, -4]

sol = Solution()
print(sol.threeSum(nums))
