"""
To run this file issue this command:
python3 HelloWorld.py

Python as a interpreted language executes code directly without a separate compilation step, 
translating and running the source code on-the-fly during execution.
"""
import sys
from HelloWorld import HelloWorld


# Checks if the Python script is being run as the main program (not imported as a module)
import sys
import random

def shell_sort(arr):
    length = len(arr)
    gap = [1]
    k=0
    #generating the gap using Segwick's formula
    while True:
        tmp=(4**(k+1))+(3*(2**k))+1 #Segwick's formula
        if tmp<=length:
            gap.append(tmp)
        else:
            break
        k+=1
    #sorting the array using the gap and insertion sort
    for i in range(len(gap)-1,-1,-1):
        for j in range(0,length,gap[i]):
            key=arr[j]
            k=j-gap[i]
            while k>=0 and arr[k]>key:
                arr[k+gap[i]]=arr[k]
                k-=gap[i]
            arr[k+gap[i]]=key
    return arr


#bringing the largest element to the top or smallest element to the bottom
#sorting is true if we are sorting the heap
#sorting is false if we are creating the heap
#index=current element index
#indexstop is used to indetify the last element in heap index (used while sorting the heap)
def heapify(arr,index,sorting,indexstop):
        if sorting==False:
            if indexstop<=(2*index)+1:
                return 0
        else:
            if indexstop<(2*index)+2:
                return 0
        #pulling down element in the heap if smallest
        if arr[(2*index)+1]>=arr[(2*index)+2] or (sorting==True and indexstop<=(2*index)+2):
            if (arr[index]<arr[(2*index)+1]) and indexstop>(2*index)+1:
                arr[index],arr[(2*index)+1]=arr[(2*index)+1],arr[index]
                heapify(arr,(2*index)+1,sorting,indexstop)
        else:
            if arr[index]<arr[(2*index)+2] and indexstop>(2*index)+2:
                arr[index],arr[(2*index)+2]=arr[(2*index)+2],arr[index]
                heapify(arr,(2*index)+2,sorting,indexstop)

def heap_sort(arr):
    length=len(arr)
    #creating the heap
    for i in range(length//2-1,-1,-1):
        if arr[(2*i)+1]>=arr[(2*i)+2]:
            arr[i],arr[(2*i)+1]=arr[(2*i)+1],arr[i]
            heapify(arr,(2*i)+1,False,length)
        else:
            arr[i],arr[(2*i)+2]=arr[(2*i)+2],arr[i]
            heapify(arr,(2*i)+2,False,length)
    #sorting the heap
    for i in range(1,length):
        arr[0],arr[length-i]=arr[length-i],arr[0]
        heapify(arr,0,True,length-i)
    return arr

def insertionSort(arr):
    length = len(arr)
    if length <= 1:
        return  # If the array has 1 or 0 elements, it's already sorted
    for i in range(1, length):
        key = arr[i]  # Select the element to be inserted
        j = i - 1  # Initialize the index of the previous element
        while j >= 0 and key < arr[j]:  # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key  # Place key at after the element just smaller than it
    return arr

def selectionSort(arr):
    length = len(arr)
    for i in range(length):
        min_index = i  # Find the minimum element in remaining unsorted array
        for j in range(i + 1, length):  # Traverse the unsorted subarray to find the minimum element
            if arr[j] < arr[min_index]:  # Update the index of the minimum element if a smaller element is found
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap the found minimum element with the first element
    return arr

def divqSort(arr, low, high, pivot_type='first'):
    """
    This function partitions the array around a pivot element.
    The pivot can be the first element or a random element.
    """
    if pivot_type == 'first':
        pivot = arr[low]  # Use the first element as pivot
    elif pivot_type == 'random':
        pivot_index = random.randint(low, high)  # Choose a random pivot
        pivot = arr[pivot_index]  # Use the random element as pivot
        arr[pivot_index], arr[low] = arr[low], arr[pivot_index]  # Swap pivot with the first element

    i = low + 1  # Initialize the smaller element index
    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:  # If current element is smaller than or equal to pivot
            arr[i], arr[j] = arr[j], arr[i]  # Swap the elements
            i = i + 1  # Increment the smaller element index

    arr[low], arr[i - 1] = arr[i - 1], arr[low]  # Swap the pivot element with the element at i-1
    return i - 1  # Return the partitioning index

def quickSort(arr, low, high, pivot_type='first'):
    """
    This function implements the QuickSort algorithm.
    It recursively sorts the array by partitioning it around a pivot element.
    The pivot can be the first element or a random element.
    """
    if low < high:
        pi = divqSort(arr, low, high, pivot_type)  # Partition the array
        quickSort(arr, low, pi - 1, pivot_type)  # Recursively sort the left subarray
        quickSort(arr, pi + 1, high, pivot_type)  # Recursively sort the right subarray
    return arr  # Return the sorted array

def sort_using_algorithm(data, algorithm):
    # This function takes the algorithm identifier as input
    # However, it always uses the sorted function in Python
    if algorithm == 1:
        sorted_data = shell_sort(data)
    elif algorithm == 2:
        sorted_data = heap_sort(data)
    elif algorithm == 3:
        sorted_data = insertionSort(data)
    elif algorithm == 4:
        sorted_data = selectionSort(data)
    elif algorithm == 5:
        sorted_data = divqSort(data)
    return sorted_data

def main():
    # Command-line arguments: python script.py --algorithm <algorithm_number>
    if len(sys.argv) != 3 or sys.argv[1] != "--algorithm":
        print("Usage: python script.py --algorithm <algorithm_number>")
        sys.exit(1)

    algorithm_number = int(sys.argv[2])

    # Read input data from standard input until the end of file (EOF)
    input=sys.stdin.read().split()
    try:
        data = [int(x) for x in input[1:]]
    except EOFError:
        print("Error reading input.")

    # Perform sorting using the specified algorithm (ignored in this example)
    sorted_data = sort_using_algorithm(data, algorithm_number)

    # Print the sorted data
    print("Sorted data:", sorted_data[0:10])


if __name__ == "__main__":
    main()
