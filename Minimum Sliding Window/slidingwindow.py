class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = {}

        # Frequency of characters needed
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        required = len(need)      # Number of unique characters needed
        formed = 0                # Number of unique characters currently satisfied

        window = {}

        left = 0
        ans_len = float('inf')
        ans_start = 0

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                formed += 1

            # Try shrinking the window
            while formed == required:

                if right - left + 1 < ans_len:
                    ans_len = right - left + 1
                    ans_start = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        if ans_len == float('inf'):
            return ""

        return s[ans_start:ans_start + ans_len]
