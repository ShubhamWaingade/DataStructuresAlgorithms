​The important thing to consider here are the addtitional information given, we are instructed to assume that;
nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array. Based on this condition we need to consider tow additional edge cases here `if(nums[0] > nums[1]){return 0;}` 
and `if (nums[numsLen-1] > nums[numsLen-2]){return numsLen -1;}` 

### Moving forwerd it is important to note this instance that when ever there is an additional condition is given, 
### there has to be either a corner case or twist in the implementation