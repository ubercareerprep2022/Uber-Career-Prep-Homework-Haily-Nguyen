"""
Haily Nguyen, UCP 2022, Aug 11

Sorting Exercise 2: External Sort
Given a large array containing a million entries, sort them by loading only
100 entries at a time in memory.
"""

import numpy as np
import shutil
import os
import heapq


# buffer size is the max number your memory can handle, set a small number in the beginning for trial here
buffer_size = 50000
# total size of the number that needs to be sorted, only needed if you want to generate a file of unsorted integers
total_size = 10000

"""
Helper functions to save array to file, sort and write, generate a csv file with unsorted numbers 
"""


def save_array_to_file(file_name, array_to_save):
    np.savetxt(file_name, array_to_save, fmt='%d')


def sort_and_write(file_name, array_to_sort):
    array_to_sort.sort()
    save_array_to_file(file_name, array_to_sort)


def read_n_int(file_, numbers_to_read):
    array_ = []

    if numbers_to_read <= 0:
        return array_

    num = file_.readline()
    while (num):
        array_.append(int(num))
        if len(array_) >= numbers_to_read:
            break
        num = file_.readline()

    return array_


def create_unsorted_file(size_, file_name_='unsorted.csv'):
    arr = np.arange(size_)
    np.random.shuffle(arr)
    save_array_to_file(file_name_, arr)
    arr = None


create_unsorted_file(total_size, file_name_='unsorted.csv')

"""
Methods to execute External Sort
1. Read as many numbers from the input file as the memory can handle at a time, 
   sort them using quick sort. Write the sorted numbers in a file.
2. Merge the numbers from the intermediate files: 
   Use a data structure called min heap. 
   A min heap always keeps minimum number at the root node. 
   a. Read smallest value from each file 
   (which will be the first value because all the files are sorted), 
   b. Insert them into a min heap. It will maintain minimum at the top of the heap. 
   c. Draw minimum from the min heap and add it to the output file. 
   d. Since we removed an element from the heap, we will add a new element from the 
   same file from which it was drawn. For example, if we have four intermediate files 
   named output 1, output 2, output 3, output 4, and the last min drawn from the min 
   heap belonged to file output 3, then we will read next number from the output 3 and 
   add it to the heap. 
   e. Then we will draw min from the heap again and continue the process until all the 
   numbers written to the output file. 
   
In total, the second step takes O (n log k) time, where n is the number of elements in 
the input file and k is the number of intermediate files we create.
"""


# Part 1
def sort_slices(file_name, buffer_size_):
    read_arr = []
    chunk = 1
    f = open(file_name)

    if os.path.exists('./tmp/'):
        shutil.rmtree('./tmp/')
    os.mkdir('./tmp/')

    # TODO : delete contents of tmp directory
    read_arr = read_n_int(f, buffer_size_)
    while len(read_arr) > 0:
        sort_and_write('./tmp/sorted_' + str(chunk), read_arr)
        read_arr = read_n_int(f, buffer_size_)
        chunk = chunk + 1

    f.close()


# Part 2
def min_heap_sort(output_file):
    sorted_file = open(output_file, 'w+')
    min_heap = []
    heapq.heapify(min_heap)

    open_files = []
    for f in os.listdir('./tmp/'):
        if os.path.isfile('./tmp/' + f):
            file_ = open('./tmp/' + f)
            open_files.append(file_)
            val = file_.readline()
            heapq.heappush(min_heap, (int(val), file_))

    while len(min_heap) > 0:
        # Draw minimum from the min heap
        min_element = heapq.heappop(min_heap)
        # Add it to the output file
        sorted_file.write(str(min_element[0]) + '\n')
        # Add a new element from the same file from which it was drawn
        next_str = min_element[1].readline()
        if next_str:
            heapq.heappush(min_heap, (int(next_str), min_element[1]))
        else:
            min_element[1].close()

    sorted_file.close()


def external_sort(input_file, output_file, buffer_size_=10000):
    sort_slices(input_file, buffer_size_)
    min_heap_sort(output_file)
    print('Sorted values are written to', str(output_file))


external_sort(input_file='unsorted.csv', output_file='sorted_external.csv', buffer_size_=buffer_size)

