def find_word_with_prefix_suffix(words, n, q):
    """
    Finds the index of the word in the list that has both the given prefix and suffix.

    Args:
        words: A list of words (strings).
        n: The number of words in the list.
        q: The number of queries.

    Returns:
        A list of integers, where each element represents the index of the word
        found for the corresponding query. If no such word exists, -1 is returned.
    """

    word_trie = dict()  # Create a trie to efficiently handle prefix searches

    def insert_word(word):
        """Inserts a word into the trie."""
        current_node = word_trie
        for char in word:
            if char not in current_node:
                current_node[char] = dict()
            current_node = current_node[char]

    # Construct the trie for efficient prefix searches
    for word in words:
        insert_word(word)

    def find_match(prefix, suffix):
        """Searches for a word with the given prefix and suffix using the trie."""
        current_node = word_trie
        for char in prefix:
            if char not in current_node:
                return -1  # Prefix not found in the trie
            current_node = current_node[char]

        # Search for the suffix starting from the last matching node in the prefix search
        suffix_chars = set(suffix)
        node_stack = [current_node]

        while node_stack:
            current_node = node_stack.pop()
            if suffix_chars == set():  # All suffix characters matched
                return max(index for index, word in enumerate(words) if word.startswith(prefix))
            if not current_node:
                continue  # Reached an empty node without matching the suffix
            node_stack.extend(current_node.values())
            suffix_chars.discard(min(suffix_chars))  # Process characters in lexicographic order

        return -1  # No word found with the given prefix and suffix

    results = []
    for _ in range(q):
        prefix, suffix = input().split()
        results.append(find_match(prefix, suffix))

    return results

if __name__ == "__main__":
    n, q = map(int, input().split())
    words = input().split()
    results = find_word_with_prefix_suffix(words, n, q)
    for result in results:
        print(result)
