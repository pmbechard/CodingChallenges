"""
804. Unique Morse Code Words
https://leetcode.com/problems/unique-morse-code-words/
"""


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                       "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        result = []
        for word in words:
            transformation = ""
            for letter in word:
                transformation += morse_codes[ord(letter) - 97]
            if transformation not in result:
                result.append(transformation)
        return len(result)
