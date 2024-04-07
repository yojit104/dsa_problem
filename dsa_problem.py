input_arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def max_sum_subarray(A):
    N = len(A)

    if N == 0:
        return "invalid input"
    
    max_ending_here = 0
    max_so_far = float('-inf')
    
    for i in range(N):
        max_ending_here += A[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far

print(max_sum_subarray(input_arr))
