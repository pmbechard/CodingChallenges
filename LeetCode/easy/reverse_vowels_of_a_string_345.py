"""
345. Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [x for x in s if x.lower() in 'aeiou'][::-1]
        consonants = [x for x in s if x.lower() not in 'aeiou']
        results = ''
        v_index, c_index = 0, 0
        for i in s:
            if i.lower() in 'aeiou':
                results += vowels[v_index]
                v_index += 1
            else:
                results += consonants[c_index]
                c_index += 1
        return results
