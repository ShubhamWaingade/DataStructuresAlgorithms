class Solution:
    def mergeArr(self, integer_arr, temp_arr, lower_bound, mid_index, upper_bound):
        left_ind = lower_bound
        iterator_index = lower_bound
        right_ind = mid_index + 1

        while left_ind <= mid_index and right_ind <= upper_bound:
            if integer_arr[left_ind] <= integer_arr[right_ind]:
                temp_arr[iterator_index] = integer_arr[left_ind]
                left_ind += 1
            else:
                temp_arr[iterator_index] = integer_arr[right_ind]
                right_ind += 1
            iterator_index += 1
        
        while left_ind <= mid_index:
            temp_arr[iterator_index] = integer_arr[left_ind]
            left_ind += 1
            iterator_index += 1

        while right_ind <= upper_bound:
            temp_arr[iterator_index] = integer_arr[right_ind]
            right_ind += 1
            iterator_index += 1


        for temp_ind in range(lower_bound, upper_bound+1):
            integer_arr[temp_ind] = temp_arr[temp_ind]

    def mergeSort(self, integer_arr, temp_arr, lower_bound, upper_bound):
        if lower_bound >= upper_bound:
            return
        mid_index = lower_bound + (upper_bound - lower_bound) // 2
        self.mergeSort(integer_arr, temp_arr, lower_bound, mid_index)
        self.mergeSort(integer_arr, temp_arr, mid_index+1, upper_bound)
        self.mergeArr(integer_arr, temp_arr, lower_bound, mid_index, upper_bound)


    def sortArray(self, nums: List[int]) -> List[int]:
        arr_len = len(nums)
        temp_arr = [0] * arr_len
        lower_bound = 0
        self.mergeSort(nums, temp_arr, 0, arr_len-1)
        return nums
