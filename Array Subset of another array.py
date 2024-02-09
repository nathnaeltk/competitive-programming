#User function Template for python3

def isSubset(a1, a2, n, m):
    freq_a1 = {}
    freq_a2 = {}

    for elem in a1:
        freq_a1[elem] = freq_a1.get(elem, 0) + 1

    for elem in a2:
        freq_a2[elem] = freq_a2.get(elem, 0) + 1

    for elem, count_a2 in freq_a2.items():
        count_a1 = freq_a1.get(elem, 0)
        if count_a1 < count_a2:
            return "No"

    return "Yes"
