"""
819. Most Common Word
https://leetcode.com/problems/most-common-word/
"""


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub('[^a-zA-Z0-9 ]', ' ', paragraph).lower().split()
        paragraph_set = set(paragraph)
        paragraph_set.difference_update(banned)
        output = None
        output_count = 0
        for i in paragraph_set:
            if paragraph.count(i) > output_count:
                output_count = paragraph.count(i)
                output = i
        return output
