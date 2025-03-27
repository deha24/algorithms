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
#bringing the largest element to the top or smallest element to the bottom
#sorting is true if we are sorting the heap
#sorting is false if we are creating the heap
#index=current element index
#indexstop is used to indetify the last element in heap index (used while sorting the heap)
def heapify(arr,index,sorting,indexstop):
        right_child=(2*index)+2
        left_child=(2*index)+1 
        if sorting==False:
            if indexstop<=left_child:
                return 0
        else:
            if indexstop<right_child:
                return 0
        #pulling down element in the heap if smallest
        if indexstop<=right_child or arr[left_child]>=arr[right_child]:
            if (arr[index]<arr[left_child]) and indexstop>left_child:
                arr[index],arr[left_child]=arr[left_child],arr[index]
                heapify(arr,left_child,sorting,indexstop)
        else:
            if arr[index]<arr[right_child] and indexstop>right_child:
                arr[index],arr[right_child]=arr[right_child],arr[index]
                heapify(arr,right_child,sorting,indexstop)

def heap_sort(arr):
    length=len(arr)
    #creating the heap
    for i in range(length//2-1,-1,-1):
        right_child=(2*i)+2
        left_child=(2*i)+1
        if right_child<length and arr[left_child]>=arr[right_child] and arr[i]<arr[left_child]:
            arr[i],arr[left_child]=arr[left_child],arr[i]
            heapify(arr,left_child,False,length-1)
        elif right_child>=length and arr[i]<arr[left_child]:
            arr[i],arr[left_child]=arr[left_child],arr[i]
            heapify(arr,left_child,False,length-1)
        elif right_child<length and arr[i]<arr[right_child]:
            arr[i],arr[right_child]=arr[right_child],arr[i]
            heapify(arr,right_child,False,length-1)
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

# Function to partition the array using the median-of-three pivot strategy
def divqSort(arr, low, high):
    # Calculate the middle index
    mid = (low + high) // 2
    # Select pivot candidates (first, middle, last elements)
    pivot_candidates = [(arr[low], low), (arr[mid], mid), (arr[high], high)]
    # Sort pivot candidates by value
    pivot_candidates.sort(key=lambda x: x[0])
    # Choose the median as the pivot
    pivot_index = pivot_candidates[1][1]
    # Swap the pivot with the first element
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
    pivot = arr[low]
    i = low + 1
    # Partition the array around the pivot
    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    # Place the pivot in its correct position
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

# Helper function for iterative quicksort using the median-of-three pivot
def quickSortHelper(arr, low, high):
    # Use a stack to simulate recursion
    stack = [(low, high)]
    while stack:
        low, high = stack.pop()
        while low < high:
            # Partition the array and get the pivot index
            pi = divqSort(arr, low, high)
            # Push the larger partition onto the stack to minimize stack size
            if pi - low < high - pi:
                stack.append((pi + 1, high))
                high = pi - 1
            else:
                stack.append((low, pi - 1))
                low = pi + 1
    return arr

# Function to perform quicksort using the median-of-three pivot
def quickSort(arr):
    return quickSortHelper(arr, 0, len(arr) - 1)

# Function to partition the array using the leftmost element as the pivot
def divqSortleftpivot(arr, low, high):
    # Base case: if the subarray is already sorted or has identical elements
    if low >= high or all(arr[k] == arr[low] for k in range(low, high + 1)):
        return low
    pivot = arr[low]
    i = low + 1
    # Partition the array around the pivot
    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    # Place the pivot in its correct position
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

# Helper function for iterative quicksort using the leftmost pivot
def quickSortleftpivotHelper(arr, low, high):
    # Use a stack to simulate recursion
    stack = [(low, high)]
    while stack:
        low, high = stack.pop()
        while low < high:
            # Partition the array and get the pivot index
            pi = divqSortleftpivot(arr, low, high)
            # Push the larger partition onto the stack to minimize stack size
            if pi - low < high - pi:
                stack.append((pi + 1, high))
                high = pi - 1
            else:
                stack.append((low, pi - 1))
                low = pi + 1
    return arr

# Function to perform quicksort using the leftmost element as the pivot
def quickSortleftpivot(arr):
    return quickSortleftpivotHelper(arr, 0, len(arr) - 1)

def shell_sort(arr):
    length = len(arr)
    gap = [1]
    k=0
    #generating the gap using Segwick's formula
    while True:
        tmp=(4**(k+1))+(3*(2**k))+1 #Segwick's formula
        if tmp<length:
            gap.append(tmp)
        else:
            break
        k+=1
    #sorting the array using the gap and insertion sort
    for i in range(len(gap)-1,-1,-1):
        tmp = insertionSort(arr[0:length:gap[i]])
        for j in range(len(tmp)):
            arr[j*gap[i]]=tmp[j]
            
    return arr


def sort_using_algorithm(data, algorithm):
    # This function takes the algorithm identifier as input and returns the sorted data
    if algorithm == 1:
        sorted_data = insertionSort(data)
    elif algorithm == 2:
        sorted_data = shell_sort(data)
    elif algorithm == 3:
        sorted_data = selectionSort(data)
    elif algorithm == 4:
        sorted_data = heap_sort(data)
    elif algorithm == 5:
        sorted_data = quickSortleftpivot(data)
    elif algorithm == 6:
        sorted_data = quickSort(data)
    return sorted_data


def main():
    sys.setrecursionlimit(1500)
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

    # Perform sorting using the specified algorithm
    sorted_data = sort_using_algorithm(data, algorithm_number)

    # Print the sorted data
    print("Sorted data:", sorted_data)


if __name__ == "__main__":
    main()
