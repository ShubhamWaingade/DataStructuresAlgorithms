import random

"""
This is an alternate approach which implements the Quick Sort
Average Time Complexity O(N*logN)
Space Complexity O(logN)
"""
class Solution:
    def partitionArray(self, integer_arr, lower_bound, upper_bound):
        pivot_index = random.randint(lower_bound, upper_bound)
        print(lower_bound, pivot_index, upper_bound)
        integer_arr[pivot_index], integer_arr[upper_bound]  = integer_arr[upper_bound], integer_arr[pivot_index]
        pivot_elem = integer_arr[upper_bound]
        lower_index = lower_bound - 1

        for upper_index in range(lower_bound, upper_bound):
            if integer_arr[upper_index] < pivot_elem:
                lower_index += 1
                integer_arr[lower_index], integer_arr[upper_index]  = integer_arr[upper_index], integer_arr[lower_index]
        
        integer_arr[upper_bound], integer_arr[lower_index+1] = integer_arr[lower_index+1], integer_arr[upper_bound]
        return lower_index + 1


    def quickSort(self, integer_arr, lower_bound, upper_bound):
        if lower_bound < upper_bound:
            partition_index = self.partitionArray(integer_arr, lower_bound, upper_bound)
            self.quickSort(integer_arr, lower_bound, partition_index-1)
            self.quickSort(integer_arr, partition_index+1, upper_bound)
        else:
            return

    def sortArray(self, nums):
        arr_len = len(nums)
        lower_bound = 0
        self.quickSort(nums, lower_bound, arr_len-1)
        return nums
    
# a = Solution()
# A = [5,2,3,1]
# print(a.sortArray(A))