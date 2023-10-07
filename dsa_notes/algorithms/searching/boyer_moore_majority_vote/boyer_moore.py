def boyer_moore(array: list[int]) -> int:
    """
    Find and return the majority element in an array, if it exists. A majority
    element in an array A of size n is an element that appears more than n/2
    times (> floor(n/2)).

    Args:
        array (list[int]): An array of integers, which may contain a majority
                           element.

    Returns:
        int: The majority element, or -1 if it does not exist.
    """
    n = len(array)

    # Step 1: Find a candidate for majority element.
    candidate = None
    count = 0

    for number in array:
        # Set the new candidate when count reaches 0.
        if count == 0:
            candidate = number
            count = 1

        # Increment count if num is candidate.
        elif candidate == number:
            count += 1

        # Otherwise, decrement the count.
        else:
            count -= 1

    # Step 2: Validate the candidate by ensuring it occurs more than n/2 times.
    if array.count(candidate) > n // 2:
        return candidate

    return -1


def test_boyer_moore() -> None:
    pass
