class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        have = {}
        formed = 0
        required = len(need)

        l = 0
        best_len = float("inf")
        best_start = 0

        for r in range(len(s)):
            ch = s[r]
            have[ch] = have.get(ch, 0) + 1

            # This character now satisfies its required frequency
            if ch in need and have[ch] == need[ch]:
                formed += 1

            # Window is valid
            while formed == required:
                window_len = r - l + 1

                if window_len < best_len:
                    best_len = window_len
                    best_start = l

                # Remove s[l] from the window
                left_char = s[l]
                have[left_char] -= 1

                if left_char in need and have[left_char] < need[left_char]:
                    formed -= 1

                l += 1

        if best_len == float("inf"):
            return ""

        return s[best_start:best_start + best_len]
        