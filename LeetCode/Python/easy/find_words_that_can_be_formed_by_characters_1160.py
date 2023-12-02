"""
1160. Find Words That Can Be Formed by Characters
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
"""


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # output = 0
        # for word in words:
        #     if all([i in chars and word.count(i) <= chars.count(i) for i in word]):
        #         output += len(word)
        # return output

        chars = Counter(list(chars))
        count = 0
        for word in words:
            match = True
            for char in set(word):
                if word.count(char) > chars[char]:
                    match = False
                    break
            if match:
                count += len(word)
        return count
