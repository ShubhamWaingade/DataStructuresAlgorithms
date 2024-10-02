class Solution {
    public boolean containsDuplicate(int[] nums){
        HashSet<Integer> tempSet = Arrays.stream(nums).boxed().collect(Collectors.toCollection(HashSet::new));
        return nums.length != tempSet.size();
    }
}