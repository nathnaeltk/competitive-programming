# Problem: A - Good Segment - https://codeforces.com/gym/511771/problem/A

def longest_good_segment_length(n, s):
    # Initialize variables to keep track of the longest segment and the current segment length
    max_len = 1
    current_len = 1
    
    # Iterate through the string to find the longest good segment
    for i in range(1, n):
        if ord(s[i]) == ord(s[i-1]) + 1:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
            current_len = 1
    
    # Final check to update max_len for the last segment
    if current_len > max_len:
        max_len = current_len
    
    return max_len


n = int(input())
s = input()

print(longest_good_segment_length(n, s))