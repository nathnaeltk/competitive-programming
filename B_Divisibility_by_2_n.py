# Number of test cases
test_cases = int(input())

# Loop through each test case
for _ in range(test_cases):
    # Length of the array
    array_length = int(input())
    # Array of positive integers
    array = list(map(int, input().strip().split()))

    # Initialize the count of operations needed to make the product divisible by 2^n
    ans = 0

    # Function to count the number of factors of 2 in a number
    def count_factors_of_2(check, count):
        # Keep dividing by 2 until check is no longer divisible by 2
        while check % 2 == 0:
            check //= 2
            count += 1
        return count

    # Count the total number of factors of 2 in the array
    total_factors_of_2 = 0
    for number in array:
        total_factors_of_2 += count_factors_of_2(number, 0)

    # If the total factors of 2 in the array is already greater than or equal to 2^n,
    # no operations are needed
    if total_factors_of_2 >= array_length:
        print(0)
        continue  # Move to the next test case

    # Initialize a list to store the difference between n and each index i
    difference_list = [array_length - i for i in range(array_length)]

    # Initialize a list to store the factors of 2 for each difference
    factors_of_2_list = []
    for difference in difference_list:
        factors_of_2 = 0
        # Count factors of 2 for each difference
        while difference % 2 == 0:
            factors_of_2 += 1
            difference //= 2
        factors_of_2_list.append(factors_of_2)

    # Sort the factors of 2 list in descending order
    factors_of_2_list = sorted(factors_of_2_list, reverse=True)

    # Initialize variables
    i = 0  # Index to iterate through the factors of 2 list
    f = 0  # Flag to check if the answer is found

    # Iterate through the factors of 2 list
    while i < array_length:
        # If adding factors of 2 to the total factors of 2 is enough to make it greater than or equal to 2^n,
        # print the index i + 1 and set the flag
        if factors_of_2_list[i] + total_factors_of_2 >= array_length:
            print(i + 1)
            f = 1
            break
        else:
            # Increment the total factors of 2 and move to the next index
            total_factors_of_2 += factors_of_2_list[i]
            i += 1
    
    # If the flag is set, move to the next test case
    if f:
        continue

    # If the flag is not set, print -1
    print(-1)
