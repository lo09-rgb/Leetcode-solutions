class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)

        current = 1

        # Left products
        for i in range(len(nums)):
            left[i] = current
            current *= nums[i]

        current = 1

        # Right products
        for i in range(len(nums)-1, -1, -1):
            right[i] = current
            current *= nums[i]

        answer = []

        # Final answer
        for i in range(len(nums)):
            answer.append(left[i] * right[i])

        return answer
        