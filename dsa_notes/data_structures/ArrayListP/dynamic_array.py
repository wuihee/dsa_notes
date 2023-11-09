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

    def append(self, value: T) -> None:
        """
        Append a value to the end of the array. If it's at its maximum
        capacity, extend it.

        Args:
            value (T): The value to add the array.
        """
        if self._size + 1 > self._capacity:
            new_capacity = self._capacity * 2 if self._capacity > 0 else 1
            new_array = [None for _ in range(new_capacity)]

            for i in range(len(self._array)):
                new_array[i] = self._array[i]
            self._array = new_array

        self._array[self._size] = value
        self._size += 1

    def remove_at(self, i: int) -> None:
        """
        Remove element at index i.

        Args:
            i (int): The index at which to remove the element from.

        Raises:
            IndexError: If i is not within the array.
        """
        if i < 0 or i > self._size - 1:
            raise IndexError

        for j in range(i, self._size - 1):
            self._array[j] = self._array[j + 1]
        self._array[j] = None

        self._size -= 1
