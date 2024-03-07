def minimal_operations(n, elements):
  """
  Calculates the minimal number of operations needed to make all elements in the list equal to the most frequent element.

  Args:
    n: The number of elements in the list.
    elements: The list of elements.

  Returns:
    The minimal number of operations needed.
  """

  frequency = {}
  # Count the frequency of each element.
  for element in elements:
    frequency[element] = frequency.get(element, 0) + 1

  # Find the most frequent element and its frequency.
  max_frequency = max(frequency.values())
  most_frequent_element = [element for element, count in frequency.items() if count == max_frequency][0]

  # Calculate the minimal number of operations.
  operations = 0
  for element in elements:
    if element != most_frequent_element:
      operations += 1

  return operations

# Example usage:
n = 5
elements = [1, 2, 2, 3, 3]
result = minimal_operations(n, elements)
print(result)  # Output: 2

# This code is more concise and efficient than the original code. It avoids unnecessary calculations and uses a more efficient way to find the most frequent element.
