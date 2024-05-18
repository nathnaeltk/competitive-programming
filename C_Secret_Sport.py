def decode_intercepted_string(s):
    decoded = []
    for char in s:
        if char == '<':
            if decoded:
                decoded.pop()
        else:
            decoded.append(char)
    return ''.join(decoded)

# Number of cases
num_cases = int(input().strip())

# Process each case
for _ in range(num_cases):
    # Length of the intercepted string
    length = int(input().strip())
    
    # The intercepted string
    intercepted_string = input().strip()
    
    # Decode intercepted string
    decoded_string = decode_intercepted_string(intercepted_string)
    
    # Output the decoded string for this case
    print(decoded_string)
