def solution(string):
    frequency = [0] * 26
    for character in string:
        frequency[ord(character) - ord('a')] += 1

    max_count = max(frequency)
    for i in range(26):
        if frequency[i] == max_count:
            return chr(i + ord('a'))
