We have to look at this problem from right to left (from the end of the list)
Lets understand this using an example
[1, 2, 3, 4, 7, 6, 5, 2]

From the right elements are in ascending order till the element 7, next element is smaller 4. This is the pivot element.
Inorder to find the next permutation we need to replace this 4 with the immediate greater value than 4. If we scan from the right the immediate greater value than 4 is 5. Now the list becomes
[1, 2, 3, '5', 7, 6, '4', 2] ('' are used to heilight the swapped numbers)

After this step the numbers are not the next permutation. The next step is to reverse the oder of all the elements after the swapped pivot element 5. i.e. to reverse the order of 7, 6, 4, 2

[1, 2, 3, 5, 2, 4, 6, 7]
Which becomes the required answer