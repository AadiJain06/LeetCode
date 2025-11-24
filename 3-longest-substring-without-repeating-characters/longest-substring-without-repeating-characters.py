class Solution:
    def lengthOfLongestSubstring(self, s:str) ->int:
        n = len(s)
        low = 0
        res = float('-inf')
        f = {}

        for high in range(n):
            # add current char
            f[s[high]] = f.get(s[high], 0) + 1

            length = high - low + 1

            # shrink while duplicates exist
            while len(f) < length:
                f[s[low]] -= 1
                if f[s[low]] == 0:
                    del f[s[low]]
                low += 1
                length = high - low + 1

            # update answer
            res = max(res, high - low + 1)

        if res == float('-inf'):
            return 0
        return res

        # def lengthOfLongestSubstring(self, s: str) -> int:
