"""
https://leetcode.com/problems/longest-palindromic-substring/
?envType=problem-list-v2&envId=string
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandFromCenter(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        longest_palindromic_substring: str = ""
        for i in range(len(s)):
            odd_length_palindromic_substring: str = expandFromCenter(i, i)
            even_length_palindromic_substring: str = expandFromCenter(i, i + 1)
            if len(odd_length_palindromic_substring) > len(
                longest_palindromic_substring
            ):
                longest_palindromic_substring = odd_length_palindromic_substring
            if len(even_length_palindromic_substring) > len(
                longest_palindromic_substring
            ):
                longest_palindromic_substring = even_length_palindromic_substring
        return longest_palindromic_substring
