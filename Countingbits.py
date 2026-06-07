class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = []

        for i in range(n + 1):
            count_one = 0

            for b in bin(i):
                if b == '1':
                    count_one += 1

            ans.append(count_one)

        return ans
