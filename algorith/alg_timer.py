from random import randint
from timeit import repeat


def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

#    print(f"from __main__ import {algorithm}"
#          if algorithm != "sorted" else "default sort algorithm")

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")
    print(f"Algorithm: {algorithm}. Execution time: {times}")


def bubble_sort(array):
    n = len(array)

    for i in range(n):
        sorted = True

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                sorted = False
        if sorted:
            break

    return array


def insertion_sort(array):
    print(array)
    n = len(array)
    
    for i in range(1, n):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:
            print(f"{array[j]} > {key}")
            print(f"{array[j+1]} = {array[j]}")
            array[j + 1] = array[j]
            j -= 1
            print (f"\t\t array {array}")

        array[j + 1] = key

        print(f"array {array} \n")
    return array


def merge_sort(array, position: str = 'N'):
    if len(array) < 2:
        return array

    midpoint = len(array) // 2
    return merge(left=merge_sort(array[:midpoint], 'left'), right=merge_sort(
        array[midpoint:], 'right'))


def merge(left, right):

    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    result = []
    left_index = right_index = 0

    while len(result) < len(left) + len(right):
        #        print(f'left_index {left_index} right_index {right_index}')
        #        print(f'{left[left_index]} <= {right[right_index]}')

        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

        if right_index == len(right):
            result += left[left_index:]
            break

        if left_index == len(left):
            result += right[right_index:]
            break

    return result


def quick_sort(array, level: str = 'def'):
    if len(array) < 2:
        return array
    low, same, high = [], [], []
    pivot = array[randint(0, len(array) - 1)]

#    print(f'array -> {array} level -> {level}  pivot -> {pivot} \n')

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

#    print(f'low -> {low} high -> {high} same -> {same} ')
#    print(f'return -> {low}{same}{high}')
    return quick_sort(low, 'low') + same + quick_sort(high, 'high')


def insertion_sort_insert(array, left, right=None):
    print(f'left -> {left} right(min) -> {right}')
    if right is None:
        right = len(array) - 1

    for i in range(left + 1, right + 1):
        print(f'for {i} in range {left + 1}, {right + 1}')
        key_item = array[i]
        j = i - 1

        print(f'[j+1] -> {j+1} key_item -> {key_item} =  {array[j + 1]} = {array[j]}')
  
        while j >= left and array[j] > key_item:
            print(f'[j+1] -> {j+1} key_item -> {key_item} =  {array[j + 1]} = {array[j]}')
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item
    
#    print(f'array -> {array}')

    return array


def timsort(array):
    min_run = 32
    n = len(array)

    for i in range(0, n, min_run):
#        print(f' min(({i} + {min_run} + 1), {n} - 1)')
        insertion_sort(array, i, min((i + min_run + 1), n - 1))


ARRAY_LENGTH = 75 

if __name__ == "__main__":
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

#    run_sorting_algorithm(algorithm="sorted", array=array)
#    run_sorting_algorithm(algorithm="merge_sort", array=array)
#    run_sorting_algorithm(algorithm="insertion_sort", array=[5,9,4,3,6,7])
#    run_sorting_algorithm(algorithm="bubble_sort", array=array)
#    run_sorting_algorithm(algorithm="quick_sort", array = array)
#    timsort(array)

    insertion_sort([5,9,7,8,4,3,1])
    
