# -*- coding: utf-8 -*-


import ctypes

MIN_CAPACITY = 16

"""
DynArray is class which represents container for dynamic array.
Minimum array capacity is 16.
Increase buffer coefficient is 2
Decrease buffer coefficient is 1.5
"""
class DynArray:
    def __init__(self):
        """ Variable and memory initiation """
        self.capacity = 16
        self.count = 0
        self.array = self.make_array(self.capacity)

    def __len__(self):
        """
        Magic method for len()
        :return count of elements
        """
        return self.count

    def make_array(self, new_capacity):
        """
        Allocator for new array data
        :param new_capacity: new allocated data
        :return: new array data
        """
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        """
        Magic method for "[]"
        :param i: index of received element
        :return: element at "i" index
        :exception IndexError thrown if index is out of bounds
        """
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[ i ]

    def resize(self, new_capacity):
        """
        Processing resize of the memory.
        Also checked min_capacity condition
        :param new_capacity: new capacity of the array
        """
        # new_capacity must be equal or more than MIN_CAPACITY
        if new_capacity < MIN_CAPACITY:
            new_capacity = MIN_CAPACITY

        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        """
        Appends data into the end of list
        :param itm: appended element
        """
        self._increase_buffer()
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        """
        Inserting new element in selected position.
        :param i: insert index
        :param itm: inserted element
        :exception IndexError if index is out of bounds
        """
        # checking bounds
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')

        self._increase_buffer()

        # shifting all elements to the right
        for j in range(self.count, i, -1):
            # print("moving {0} from pos {1} to pos {2}".format(self.array[ j-1 ], j-1, j))
            self.array[ j ] = self.array[ j-1 ]

        # setting new element
        self.array[ i ] = itm
        self.count += 1

    def delete(self, i):
        """
        Deleting element from array.
        :param i: index of deleted element
        :exception IndexError if index is out of bounds
        """
        # checking bounds
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')

        for j in range(i, self.count-1):
            self.array[ j ] = self.array[ j+1 ]

        self.count -= 1
        self._decrease_buffer()

    def to_list(self):
        """
        Service method for converting dynamic array into standard python list
        :return: python list with array data
        """
        result = []
        for i in range(len(self)):
            result.append(self[i])
        return result

    def _increase_buffer(self):
        """
        Service private function for processing buffer increasing.
        All required checks performs here.
        """
        if self.count == self.capacity:
            self.resize(2 * self.capacity)

    def _decrease_buffer(self):
        """
        Service private function for processing buffer decreasing.
        All required checks performs here.
        """
        decrease_capacity = int(self.capacity / 1.5)
        decrease_criteria = int(self.capacity * 0.5)
        if self.count < decrease_criteria:
            self.resize(decrease_capacity)
