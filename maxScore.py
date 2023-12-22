# Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

def maxScore(self, s: str) -> int:
    L = len(s)
    left = [0 for i in range(L)]
    right = [0 for i in range(L)]
    score = [0 for i in range(L)]
    for i in range(L - 1):
        left[i] = s[0:(i + 1)].count('0')
        right[i] = s[(i + 1): L].count('1')
        score[i] = left[i] + right[i]
    return max(score)
