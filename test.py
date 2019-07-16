import unittest

from main import DynArray


def prepare_array(count):
    m = DynArray()
    for i in range(0, count):
        m.append(i)
    return m


class TestDynArray(unittest.TestCase):
    # ==================== APPEND =====================================
    def test_append_normal_case(self):
        test_data = prepare_array(10)
        test_data.append(42)
        valid_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 42]
        self.assertEqual(test_data.to_list(), valid_data,
                         "Test APPEND. Normal case. result arrays not equal")
        self.assertEqual(test_data.capacity, 16,
                         "Test APPEND. Normal case. Incorrect capacity size")

    def test_append_capacity_exceeded(self):
        test_data = prepare_array(16)
        test_data.append(42)
        valid_data = [0, 1,  2,  3,  4,  5,  6,  7, 8,
                      9, 10, 11, 12, 13, 14, 15, 42]
        self.assertEqual(test_data.to_list(), valid_data,
                         "Test APPEND. Capacity exceed case. result arrays not equal")
        self.assertEqual(test_data.capacity, 32,
                         "Test APPEND. Capacity exceed case. Incorrect capacity size")

    # ==================== GET ITEM =====================================

    def test_get_item_normal_case(self):
        test_data = prepare_array(10)
        check_data = test_data[5]
        self.assertEqual(check_data, 5,
                         "Test GET ITEM. Normal case. Received incorrect item")

    def test_get_item_negative_index_case(self):
        test_data = prepare_array(10)
        is_error = False
        try:
            check_data = test_data[-5]
        except IndexError:
            is_error = True
        self.assertEqual(is_error, True,
                         "Test GET ITEM. Negative index case. Exception wasn\'t thrown")

    def test_get_item_too_large_index_case(self):
        test_data = prepare_array(10)
        is_error = False
        try:
            check_data = test_data[10]
        except IndexError:
            is_error = True
        self.assertEqual(is_error, True,
                         "Test GET ITEM. Too large index case. Exception wasn\'t thrown")

    # ==================== INSERT =====================================

    def test_insert_normal_case(self):
        test_data = prepare_array(5)
        valid_data = [0, 1, 5, 2, 3, 4]
        test_data.insert(2, 5)
        self.assertEqual(test_data.to_list(), valid_data,
                         "Test INSERT. Normal case. Result lists are not equal.")
        self.assertEqual(test_data.capacity, 16,
                         "Test INSERT. Normal case. Capacity incorrect.")

    def test_insert_negative_index_case(self):
        test_data = prepare_array(5)
        valid_data = [0, 1, 2, 3, 4]
        is_error = False
        try:
            test_data.insert(-2, 5)
        except IndexError:
            is_error = True
        self.assertEqual(test_data.to_list(), valid_data,
                         "Test INSERT. Negative index case. Lists are not equal")
        self.assertEqual(is_error, True,
                         "Test INSERT. Negative index case. Error wasn\'t thrown")

    def test_insert_too_large_index_case(self):
        test_data = prepare_array(5)
        valid_data = [0, 1, 2, 3, 4]
        is_error = False
        try:
            test_data.insert(6, 5)
        except IndexError:
            is_error = True
        self.assertEqual(test_data.to_list(), valid_data,
                         "Test INSERT. Too large case. Lists are not equal")
        self.assertEqual(is_error, True,
                         "Test INSERT. Too large case. Error wasn\'t thrown")

    def test_insert_end_of_array_case(self):
        test_data = prepare_array(5)
        valid_data = [0, 1, 2, 3, 4, 42]
        test_data.insert(5, 42)
        self.assertEqual(test_data.to_list(), valid_data,
                         "Test INSERT. End of array case. Result lists are not equal.")

    def test_insert_buffer_increased_case(self):
        test_data = prepare_array(16)
        valid_data = [42, 0,  1,  2,  3,  4,  5,  6,  7,
                      8,  9,  10, 11, 12, 13, 14, 15]
        old_cap = int(test_data.capacity)
        test_data.insert(0, 42)
        new_cap = test_data.capacity
        self.assertEqual(test_data.to_list(), valid_data,
                         "Test INSERT. Buffer increased case. Result lists are not equal")
        self.assertEqual(old_cap, 16,
                         "Test INSERT. Buffer increased case. Source capacity was incorrect")
        self.assertEqual(new_cap, 32,
                         "Test INSERT. Buffer increased case. Result capacity was incorrect")

    # ==================== REMOVE =====================================

    def test_remove_normal_case(self):
        test_data = prepare_array(25)
        valid_data = [0,  2,  3,  4,  5,
                      6,  7,  8,  9,  10,
                      11, 12, 13, 14, 15,
                      16, 17, 18, 19, 20,
                      21, 22, 23, 24]
        test_data.delete(1)
        self.assertEqual(test_data.to_list(), valid_data,
                         "Test REMOVE. Normal case. Result lists are not equal")
        self.assertEqual(test_data.capacity, 32,
                         "Test REMOVE. Normal case. Capacity size incorrect")

    def test_remove_negative_index_case(self):
        test_data = prepare_array(5)
        valid_data = [0, 1, 2, 3, 4]
        is_error = False
        try:
            test_data.delete(-1)
        except IndexError:
            is_error = True

        self.assertEqual(test_data.to_list(), valid_data,
                         "Test REMOVE. Negative index case. Result lists are not equal")
        self.assertEqual(is_error, True,
                         "Test REMOVE. Negative index case. Error wasn\'t thrown")

    def test_remove_too_large_index_case(self):
        test_data = prepare_array(5)
        valid_data = [0, 1, 2, 3, 4]
        is_error = False
        try:
            test_data.delete(5)
        except IndexError:
            is_error = True

        self.assertEqual(test_data.to_list(), valid_data,
                         "Test REMOVE. Too large index case. Result lists are not equal")
        self.assertEqual(is_error, True,
                         "Test REMOVE. Too large index case. Error wasn\'t thrown")

    def test_decrease_buffer_case(self):
        test_data = prepare_array(20)
        valid_data = [0,  1,  2,  3,  4,  5,  6,  7,  8,  9,
                      11, 12, 13, 14, 15, 16, 17, 18, 19]
        old_cap = int(test_data.capacity)
        test_data.delete(10)
        new_cap = test_data.capacity
        self.assertEqual(test_data.to_list(), valid_data,
                         "Test REMOVE. Decrease buffer case. Result lists are not equal")
        self.assertEqual(old_cap, 32,
                         "Test REMOVE. Decrease buffer case. Old capacity was incorrect")
        self.assertEqual(new_cap, 21,
                         "Test REMOVE. Decrease buffer case. New capacity is incorrect")

    def test_remove_prevent_buffer_decreasing_with_min_cap_case(self):
        test_data = prepare_array(5)
        valid_data = [0, 2, 3, 4]
        test_data.delete(1)
        self.assertEqual(test_data.to_list(), valid_data,
                         "Test REMOVE. Prevent buffer decreasing with min capacity case."
                         "Result lists are not equal")
        self.assertEqual(test_data.capacity, 16,
                         "Test REMOVE. Prevent buffer decreasing with min capacity case."
                         "Capacity size incorrect")


if __name__ == '__main__':
    unittest.main()
