# Two-Pointer Technique

## Definition

The Standard Two-Pointer Approach involves using two pointers to traverse a linear data structure (like arrays or strings), where one pointer starts at the beginning and the other at the end, and they move towards each other. This method is often used to search for a pair of elements that meet a specific condition in a sorted array or list.

## Concept

Rather than iterating through every single element comparison, the algorithm leverages the sorted property of the data structure it is traversing to either advance the left pointer or reduce the right pointer. It often reduces the time complexity from $O(n^2)$ to $O(n)$ of searching algorithms.

## Characteristics

- **Time Complexity**: $O(n)$
- **Space Complexity**: $O(1)$
- **Prerequisites**: The data set (e.g., array or list) typically needs to be sorted.

## Algorithm

The approach uses two pointers that represent positions in the data structure. These pointers move based on some predefined conditions during each iteration, typically in a loop.

- The **left pointer** starts at the beginning (index 0 in a zero-indexed data structure like an array).
- The **right pointer** starts at the end (index `length - 1`).
- Based on a condition, we either advance the left or right pointer.

```python
if array[i] + array[j] < target:
    i += 1
elif array[i] + array[j] > target:
    j -= 1
```

- The pointers then move towards each other until they meet or until the defined condition is satisfied.

## Leetcode Problems

### Easy

- [Two Sum](https://leetcode.com/problems/two-sum/)

### Medium

- [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
- [3Sum](https://leetcode.com/problems/3sum/)
- [Container with Most Water](https://leetcode.com/problems/container-with-most-water/)
- [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
- [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
- [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

### Hard

- [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
