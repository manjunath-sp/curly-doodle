def solution(digits):
    from collections import Counter

    count = Counter(digits)

    # Make each count even
    count['1'] -= count['1'] % 2
    count['2'] -= count['2'] % 2

    # Rebuild the string with sorted digits in descending order for maximum value
    result = '2' * count['2'] + '1' * count['1']
    return result


// DONT COPY THIS - ONLY FOR TESTING
