from collections import Counter

def solution(S):
    freq = Counter(S)
    max_freq = max(freq.values())
    candidates = [char for char in freq if freq[char] == max_freq]
    return min(candidates)


if __name__ == "__main__":
    print(solution("121212"))  # Output: "2121"
    print(solution("2121122"))  # Output: "221122"
    print(solution("1111"))  # Output: "1111"