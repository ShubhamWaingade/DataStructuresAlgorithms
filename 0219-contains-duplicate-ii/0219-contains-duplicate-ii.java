class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int j) {
        HashSet<Integer> tempSet = new HashSet<Integer>();
        for (int index = 0; index < nums.length; index++) {
            if (tempSet.contains(nums[index])) return true;
            tempSet.add(nums[index]);
            if (tempSet.size() > j){
                tempSet.remove(nums[index-j]);
            }
        }
        return false;

    }
}