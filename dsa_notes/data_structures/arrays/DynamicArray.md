# Dynamic Array

## Definition

Dynamic arrays are resizable arrays, which means the size or length of the array can change dynamically. They automatically adjust their capacity as you add or remove elements.

## Characteristics

- **Dynamic Resizing**: Automatically resizes when nearing capacity.
- **Order Preservation**: Elements remain in the order they were inserted.
- **Contiguous Memory**: Despite being dynamic, elements are stored in contiguous memory locations.

## Basic Operations and their Complexity

|Operation|Average Case|Worst Case|
|:--------|:----------:|:--------:|
|Access   |O(1)        |O(1)      |
|Search   |O(n)        |O(n)      |
|Appending|O(1)*       |O(n)      |
|Insertion|O(n)        |O(n)      |
|Deletion |O(n)        |O(n)      |

(Note: Appending has an average time of O(1) but can take O(n) in cases where resizing is required.)

## Advantages

- **Flexibility**: Can grow or shrink in size as needed.
- **Direct Access**: Provides O(1) time to fetch an element at a given index.
- **Memory Efficient**: No need to allocate memory beforehand as in static arrays.

## Disadvantages

- **Unpredictable Timing**: Occasionally, operations might take longer if resizing occurs.
- **Memory Overhead**: Can sometimes use more memory than necessary, depending on the resizing strategy and the underlying implementation.
- **Not Cache-Friendly**: Resizing operations may lead to data spread across non-contiguous memory locations, affecting cache performance.

## Real-world Applications

- Used in programming languages' standard libraries due to their flexibility (e.g., Python's list, Java's ArrayList).
- Frequently used in scenarios where the exact size of data is unpredictable.

## Pseudocode Examples

**Appending an element to ArrayList**:

```text
Function append(arrayList, value):
    If arrayList is full:
        Resize arrayList to a larger capacity
    Append value to the end of arrayList
```

## Implementation Tips

- Consider initial capacity wisely to prevent frequent resizing.
- While ArrayLists in many standard libraries handle resizing automatically, it's beneficial to understand the underlying mechanics, especially if you're implementing one from scratch.

## References
