class Logic:
    # この中に解答を記述してください
    """
    -- About reset_array_of_each_nums --
    use reset dict items in sort function
    """
    def reset_array_of_each_nums(self):
        array_of_each_nums = {
            '0' : [],
            '1' : [],
            '2' : [],
            '3' : [],
            '4' : [],
            '5' : [],
            '6' : [],
            '7' : [],
            '8' : [],
            '9' : [],
        }
        return array_of_each_nums
            
    # main sort function
    def sort(self, array, MAX_DIGITS):
        """
        -- About values --
        - array_of_each_nums: dict , classify from 0 to 9, value is list
        - new_array: for update array
        - sorted_array: result array in this function
        """
        array_of_each_nums = {
            '0' : [],
            '1' : [],
            '2' : [],
            '3' : [],
            '4' : [],
            '5' : [],
            '6' : [],
            '7' : [],
            '8' : [],
            '9' : [],
        }
        new_array = []
        sorted_array = []

        """
        -- About this for loop --
        values meaning
        - num_place : a value greater than 1,
        - array_num : int value,
        - array_num_string : string value,
        - array_num_length : length of array_num,
        """
        for num_place in range(1, MAX_DIGITS+2):
            for array_num in array[:]:
                array_num_string = str(array_num)
                array_num_length = len(array_num_string)
                
                # if length of array_num shorter than the digits to sort, remove array_num from array and append it in sorted_array
                if array_num_length < num_place:
                    sorted_array.append(array_num)
                    array.remove(array_num)
                else:  
                    digits_num = array_num_string[-num_place]
                    insert_index = 0
                    if array_of_each_nums[digits_num] != []:
                        for i in array_of_each_nums[digits_num]:
                            if array_num < i:
                                break
                            else:
                                insert_index += 1
                    array_of_each_nums[digits_num].insert(insert_index, array_num)

            # update the array
            for value_list in array_of_each_nums.values():
                new_array += value_list
            array = new_array

            # reset values
            new_array = []
            array_of_each_nums = self.reset_array_of_each_nums()
        
        return sorted_array
