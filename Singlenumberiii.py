class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        ans = []

        for num, count in freq.items():
            if count == 1:
                ans.append(num)

        return ans
