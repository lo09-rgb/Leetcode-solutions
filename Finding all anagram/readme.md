class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        p_count = [0] * 26
        window = [0] * 26

        for c in p:
            p_count[ord(c) - ord('a')] += 1

        for c in s[:len(p)]:
            window[ord(c) - ord('a')] += 1

        ans = []

        if window == p_count:
            ans.append(0)

        for i in range(len(p), len(s)):
            window[ord(s[i]) - ord('a')] += 1
            window[ord(s[i - len(p)]) - ord('a')] -= 1

            if window == p_count:
                ans.append(i - len(p) + 1)

        return ans
