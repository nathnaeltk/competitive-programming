class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word_string1 = ""
        word_string2 = ""
        for i in word1:
            word_string1 += i
        for i in word2:
            word_string2 += i
        return word_string1 == word_string2