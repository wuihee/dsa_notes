def two_pointer(array: list[int], target) -> list[int, int]:
    """
    Uses the two-pointer technqiue to find a pair of integers that sum to
    target in O(n) time.

    Args:
        array (list[int]): Integer array.
        target (_type_): Find two integers that sum to target.

    Returns:
        list[int, int]: The value of the two integers, or [-1, -1]
                        if no target found.
    """

    # array needs to be sorted for two-pointer to work.
    array.sort()

    n = len(array)
    i = 0
    j = n - 1

    while i < j:
        total = array[i] + array[j]

        # If the current sum is less than target, we "increase" the sum by
        # incrementing i. Since array is sorted, we know that array[i + 1] >
        # array[i].
        if total < target:
            i += 1

        # Likewise, if the current sum is greater than target, we decrease the
        # sum by decreaseing j by 1.
        elif total > target:
            j -= 1

        else:
            return [array[i], array[j]]

    return [-1, -1]


def test_two_pointer():
    array = [3, 2, 5, 6, 7, 1]
    print(two_pointer(array, 11))


if __name__ == "__main__":
    test_two_pointer()
