# Boyer-Moore Majority Vote Algorithm

## Definition

The Boyer-Moore Majority Vote Algorithm is an algorithm designed to find the majority element in a sequence, i.e., an element that appears more than `n / 2` times in an array of `n` elements.

## Intuition

The core insight of the algorithm is that if we cancel out the majority element with any other element (non-majority), the majority element will still remain the majority in the remaining elements.

## Characteristics

- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

## Algorithm

1. **Candidate**: Maintain a candidate for the majority element.
2. **Counter**: Maintain a counter, which counts the net number of times the majority element has been seen so far.
3. If the counter is zero, we set a new candidate for the majority element and reset the counter to 1.
4. If the counter is not zero, we increment or decrement the counter based on whether the next element is the same as the current candidate.
5. After one pass through the array, the candidate is the majority element, but a second pass must confirm it.
6. For the variant where we need to find elements that appear more than `n / 3` times, a similar yet slightly tweaked method applies. We need to maintain two candidates and their respective counters because there can be at most two elements that appear more than `n / 3` times in the array.

## Leetcode Problems

1. [Majority Element I](https://leetcode.com/problems/majority-element/description/)
2. [Majority Element II](https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05)
