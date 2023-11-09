class DynamicArray:
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
        self.array = array
        self.size = len(array)

    def size(self) -> int:
        """
        Return the size of the array.

        Returns:
            int: The number of elements in the array.
        """
        return self.size
