​​The main idea here is to find the point of convergence. 
If we go from left to right there is a point where the left pointer value becomes less than the right pointer value as it is stated that this is a sorted rotated array in ascending order.
When mid > left then move the left to mid + 1 as none of the elements between left and mid will be minimum, until the convergence point is reached.
Alternately if mid is less than right and we move the right to mid and not to mid - 1, as there is possibility that that mid point can be the minimum value