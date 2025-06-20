def solution(A, B):
    total_a_array = sum(A)
    total_b_array = sum(B)

    fair_index_count = 0
    sum_a_array = 0
    sum_b_array = 0

    for k in range(1, len(A)):  # K must be from 1 to N-1 to ensure two non-empty parts
        sum_a_array += A[k - 1]
        sum_b_array += B[k - 1]

        if (sum_a_array == total_a_array - sum_a_array and
                sum_b_array == total_b_array - sum_b_array and
                sum_a_array == sum_b_array):
            fair_index_count += 1

    return fair_index_count



# DO NOT COPY THIS
if __name__ == "__main__":
    A = [2, -2, -3, 3]
    B = [0, 0, 4, -4]
    print(solution(A, B))
