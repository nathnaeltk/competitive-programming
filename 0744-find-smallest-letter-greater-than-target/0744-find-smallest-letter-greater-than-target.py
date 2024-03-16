class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        smallest_greater = None
        for letter in letters:
            if letter > target:
                smallest_greater = letter
                break
        return smallest_greater if smallest_greater is not None else letters[0]
