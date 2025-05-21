"""
68. Text Justification
https://leetcode.com/problems/text-justification/
"""


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        curr = ''
        result = []
        while len(curr) <= maxWidth:
            if not words:
                if curr:
                    result.append(curr + ' ' * (maxWidth - len(curr)))
                break
            word = words.pop(0)
            if len(word) == maxWidth:
                if curr:
                    curr = self.fill_spaces(curr, maxWidth)
                    result += [curr]
                result += [word]
                curr = ''
            elif len(curr) + len(word) + 1 > maxWidth:
                curr = self.fill_spaces(curr, maxWidth)
                result += [curr]
                curr = word
            else:
                curr += f' {word}' if curr else word
        return result

    def fill_spaces(self, s, maxWidth):
        spaces = s.count(' ')
        diff = maxWidth - len(s) + spaces
        if spaces != 0:
            div = diff // spaces
        else:
            div = maxWidth - len(s)
        justified_spaces = ' ' * div
        s = s.replace(' ', justified_spaces, spaces)
        i = -1
        while len(s) < maxWidth:
            i = s.find(' ', i + 1)
            if i == -1:
                s = s + (' ' * (maxWidth - len(s)))
                break
            else:
                s = s[:i] + ' ' + s[i:]
                i += 1
        return s
