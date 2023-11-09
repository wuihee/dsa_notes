from typing import Generic, TypeVar

T = TypeVar("T")


class DynamicArray(Generic[T]):
    """
    Python 'implementation' of a dynamic array. We pretend to use an immutable
    array.
    """

    def __init__(self, array=[]) -> None:
        """
        Initialize the DynamicArray.

        Args:
            array (list, optional): List of elements to initialize the array
                                    with. Defaults to [].
        """
        self._array = array
        self._size = len(array)
        self._capacity = self._size

    def size(self) -> int:
        """
        Return the size of the array.

        Returns:
            int: The number of elements in the array.
        """
        return self._size

    def is_empty(self) -> bool:
        """
        Check if array is empty.

        Returns:
            bool: Return True if empty else False.
        """
        return self._size == 0

    def replace(self, i: int, value: T) -> None:
        """
        Replace element at index i with a new value.

        Args:
            i (int): Index to replace at.
            value (T): New value to replace with.
        """
        self._array[i] = value

    def clear(self) -> None:
        """
        Empty the array.
        """
        self._array = [None for _ in range(self._size)]
        self._size = 0
