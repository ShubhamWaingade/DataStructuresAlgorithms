class Solution {
        public double findMedianSortedArrays(int[] nums1, int[] nums2){
        int len1 = nums1.length;
        int len2 = nums2.length;

        if(len1 > len2){
            return  findMedianSortedArrays(nums2, nums1);
        }
        int totalLength = len1 + len2;

        int startPointer = 0;
        int endPointer = len1;
        int defaultLeftSize = (len1 + len2 + 1) / 2;
        while (startPointer <= endPointer){
            int midPoint1 = (startPointer + endPointer) /2;
            int midPoint2 = defaultLeftSize - midPoint1;

            int leftPoint1 = Integer.MIN_VALUE;
            int leftPoint2 = Integer.MIN_VALUE;
            int rightPoint1 = Integer.MAX_VALUE;
            int rightPoint2 = Integer.MAX_VALUE;

            if(midPoint1 < len1){
                rightPoint1 = nums1[midPoint1];
            }
            if(midPoint2 < len2){
                rightPoint2 = nums2[midPoint2];
            }
            if(midPoint1 -1 >= 0){
                leftPoint1 = nums1[midPoint1 - 1];
            }
            if(midPoint2 -1 >= 0){
                leftPoint2 = nums2[midPoint2 -1];
            }

            if(leftPoint1 <= rightPoint2 && leftPoint2 <= rightPoint1){
                if (totalLength % 2 == 1){
                    return Math.max(leftPoint1, leftPoint2);
                }else{
                    return (Math.max(leftPoint1, leftPoint2) + Math.min(rightPoint1, rightPoint2)) / 2.0;
                }
            } else if (leftPoint1 > rightPoint2) {
                endPointer = midPoint1 - 1;
            }else{
                startPointer = midPoint1 + 1;
            }
        }
        return 0.0;
    }
}