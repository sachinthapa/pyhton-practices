from dataclasses import dataclass
from operator import attrgetter
from typing import Optional,Set,Sequence 
from  __init__ import T, S, Key 


@dataclass(order=True)
class Person:
    name: str
    surname: str


def find_index(elements, value, key = lambda x: x) -> Optional[int]:
    left, right = 0, len(elements) - 1
    print(f'value = {value}')
    print(f'key   = {key}\n')
    print(f'length = {right}')
    #print("elements =",*elements,sep = '\n',end = '\n\n')    
    while left <= right:
        middle = (left + right) // 2
        
        middle_element = key(elements[middle])
        
        print(f'element = {middle_element}, middle = {middle}')

        if middle_element == value:
            return middle
        if middle_element < value:
            left = middle + 1
        elif middle_element > value:
            right = middle - 1

def contains(elements, value, key) -> Optional[int]:
    return find_index(elements, value, key) is not None

def find_leftmost_index(elements, value, key):
    index = find_index(elements, value, key)
    if index is not None:
        while index >=0 and key(elements[index]) == value:
            index-=1
            print(f'left index = {index}')
    #    index+=1
    return index

def find_rightmost_index(elements, value, key):
    index = find_index(elements, value, key) 
    if index is not None:
        while index < len(elements) and key(elements[index]) == value:
            index+=1
            print(f'right index = {index}')
    #   index-=1
    return index

def find_all_indices(elements, value, key) -> Set[T]:
    left = find_leftmost_index(elements, value, key)
    right = find_rightmost_index(elements, value, key)
    if left and right:
        return set(range(left, right + 1))
    return set()

def find(elements, value, key = lambda x : x) -> Optional[T]:
    index = find_index(elements, value, key)
    return None if index is None else elements[index]

def find_leftmost(elements, value, key):
    index = find_leftmost_index(elements, value, key)
    return None if index is None else elements[index]

def find_rightmost(elements, value, key) -> Optional[T]:
    index = find_rightmost_index(elements, value, key)
    return None if index is None else elements[index]

def find_all_elements(elements, value, key) -> Set[T]:
    for i in find_all_indices(elements, value, key):
        print(elements[i])
   
    return {elements[i] for i in find_all_indices(elements, value, key)}

#-----------------------------------------------------------------------------------







