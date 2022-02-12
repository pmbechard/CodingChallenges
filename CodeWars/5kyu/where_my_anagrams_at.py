"""
Where my anagrams at?
https://www.codewars.com/kata/523a86aa4230ebb5420001e1
"""

anagrams = lambda word, words: [i for i in words if sorted(list(i)) == sorted(list(word))]
