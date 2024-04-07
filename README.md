# dsa_problem

we have two variables: max_so_far and max_ending_here
we iterate through the array and store the maximum subarray sum (ending at the current index) max_ending_here.
the maximum subarray sum overall is stored in max_so_far
we add the current element and see if the sum exceeds max_so_far. If it does, we update the max_so_far. If it doesn't we move on to the next index
