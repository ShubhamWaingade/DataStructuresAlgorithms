class Solution:
        def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            if len(nums1) > len(nums2):
                return self.findMedianSortedArrays(nums2, nums1)

            len_nums1 = len(nums1)
            len_nums2 = len(nums2)
            total_len = len_nums1 + len_nums2

            left_pointer = 0
            right_pointer = len_nums1

            while left_pointer <= right_pointer:
                nums1_partition_index = int((left_pointer + right_pointer) // 2)
                nums2_partition_index = (
                    int((len_nums1 + len_nums2 + 1) / 2) - nums1_partition_index
                )

                # nums1_first_partition_value = float("-INF") if nums1_partition_index == 0 else nums1[nums1_partition_index - 1]
                # nums1_second_partition_value = float("INF") if nums1_partition_index == len_nums1 else nums1[nums1_partition_index]

                # nums2_first_partition_value = float("-INF") if nums2_partition_index == 0 else nums2[nums2_partition_index - 1]
                # nums2_second_partition_value = float("INF") if nums2_partition_index == len_nums2 else nums2[nums2_partition_index]

                nums1_first_partition_value = float("-INF")
                nums2_first_partition_value = float("-INF")
                nums1_second_partition_value = float("INF")
                nums2_second_partition_value = float("INF")

                if nums1_partition_index < len_nums1:
                    nums1_second_partition_value = nums1[nums1_partition_index]
                if nums2_partition_index < len_nums2:
                    nums2_second_partition_value = nums2[nums2_partition_index]

                if nums1_partition_index - 1 >= 0:
                    nums1_first_partition_value = nums1[nums1_partition_index - 1]

                if nums2_partition_index - 1 >= 0:
                    nums2_first_partition_value = nums2[nums2_partition_index - 1]

                if (
                    nums1_first_partition_value <= nums2_second_partition_value
                    and nums2_first_partition_value <= nums1_second_partition_value
                ):
                    if total_len % 2 == 1:
                        return float(
                            max(nums1_first_partition_value, nums2_first_partition_value)
                        )
                    else:
                        return float(
                            (
                                max(
                                    nums1_first_partition_value, nums2_first_partition_value
                                )
                                + min(
                                    nums1_second_partition_value,
                                    nums2_second_partition_value,
                                )
                            )
                            / 2
                        )

                elif nums1_first_partition_value > nums2_second_partition_value:
                    right_pointer = nums1_partition_index - 1
                else:
                    left_pointer = nums1_partition_index + 1
            return 0
