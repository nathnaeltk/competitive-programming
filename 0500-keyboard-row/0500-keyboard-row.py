class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"

        output = []
        for word in words:
            word_lower = word.lower()
            if all(letters in first_row for letters in word_lower) or \
               all(letters in second_row for letters in word_lower) or \
               all(letters in third_row for letters in word_lower):
                output.append(word)

        return output