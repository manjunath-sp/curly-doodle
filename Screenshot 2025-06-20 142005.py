def solution(digits):
    # Count digits manually
    count1 = 0
    count2 = 0
    for d in digits:
        if d == '1':
            count1 += 1
        else:  # d == '2'
            count2 += 1

    # Make counts even
    if count1 % 2 != 0:
        count1 -= 1
    if count2 % 2 != 0:
        count2 -= 1

    # Build the largest number: put '2's first, then '1's
    return '2' * count2 + '1' * count1


//NOT SURE ABOUT THIS solution
