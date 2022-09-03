class Logic:
    # この中に解答を記述してください
    def sort(self, array):
        # finish recursion when it is not possible to split any more
        if len(array) <= 1:
            return array

        # --split processing
        """
        -- About Values --
        - middle: truncation, middle index when data split
        - left: Data on the left side of the split
        - right: Data on the right side of the split
        """ 
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]

        # recursion
        left = self.sort(left)
        right = self.sort(right)

        # --join processing
        i, j, k= 0, 0, 0
        left_len = len(left)
        right_len = len(right)
        while i < left_len and j < right_len:
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < left_len:
            array[k] = left[i]
            i += 1
            k += 1

        while j < right_len:
            array[k] = right[j]
            j += 1
            k += 1

        return array
