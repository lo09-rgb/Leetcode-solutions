class Solution:
    def reverseWords(self, s: str) -> str:

        # Remove leading/trailing spaces and reduce multiple spaces to one
        words = s.split()
        chars = list(" ".join(words))

        def reverse(arr, left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        n = len(chars)

        # Reverse entire string
        reverse(chars, 0, n - 1)

        # Reverse each word
        start = 0

        for end in range(n + 1):
            if end == n or chars[end] == ' ':
                reverse(chars, start, end - 1)
                start = end + 1

        return "".join(chars)