import sys
import random
#bringing the largest element to the top or smallest element to the bottom
#sorting is true if we are sorting the heap
#sorting is false if we are creating the heap
#index=current element index
#indexstop is used to indetify the last element in heap index (used while sorting the heap)
# quicksort, heap, swap insertion, shellsort sedgwick no arr
def heapify(arr,index,sorting,indexstop):
        right_child=(2*index)+2
        left_child=(2*index)+1 
        #pulling down element in the heap if smallest
        if indexstop>left_child and (indexstop<=right_child or arr[left_child]>=arr[right_child]):
            if arr[index]<arr[left_child]:
                arr[index],arr[left_child]=arr[left_child],arr[index]
                heapify(arr,left_child,sorting,indexstop)
        elif indexstop>left_child and arr[left_child]<arr[right_child]:
            if arr[index]<arr[right_child] and indexstop>right_child:
                arr[index],arr[right_child]=arr[right_child],arr[index]
                heapify(arr,right_child,sorting,indexstop)

def heap_sort(arr):
    length=len(arr)
    #creating the heap
    for i in range((length//2)-1,-1,-1):
        heapify(arr,i,False,length)
    #sorting the heap
    for i in range(1,length):
        arr[0],arr[length-i]=arr[length-i],arr[0]
        heapify(arr,0,True,length-i)
    return arr

def insertionSort(arr):
    length = len(arr)
    if length <= 1:
        return arr
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
    # Finding the minimum element in the array and swapping it with the first element
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Function to partition the array using the random pivot strategy
def divqSort(arr, low, high):
    # Select a random pivot index
    if low > high:
        return low  # Return low as the pivot index if the range is invalid
    pivot_index = random.randint(low, high)
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

# Recursive quicksort function with tail call optimization to avoid exceeding recursion limit
def quickSortHelper(arr, low, high):
    while low < high:
        # Partition the array and get the pivot index
        pi = divqSort(arr, low, high)
        # Recur on the smaller partition to minimize recursion depth
        if pi - low < high - pi:
            quickSortHelper(arr, low, pi - 1)
            low = pi + 1  # Tail call optimization
        else:
            quickSortHelper(arr, pi + 1, high)
            high = pi - 1  # Tail call optimization
    return arr

# Function to perform quicksort using a random pivot
def quickSort(arr):
    quickSortHelper(arr, 0, len(arr) - 1)#, lambda arr, low, high: random.randint(low, high))
    return arr

# Function to partition the array using the leftmost element as the pivot
def divqSortleftpivot(arr, low, high):#, pivot_f)
    if low >= high or all(arr[k] == arr[low] for k in range(low, high + 1)):
        return low
    pivot = arr[low] #pivot_f(arr, low, high)
    i = low + 1
    # Partition the array around the pivot
    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    # Place the pivot in its correct position
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

# Helper function for recursive quicksort using the leftmost pivot
def quickSortleftpivotHelper(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = divqSortleftpivot(arr, low, high)
        # Recur on the left and right partitions
        quickSortleftpivotHelper(arr, low, pi - 1)
        quickSortleftpivotHelper(arr, pi + 1, high)
    return arr

# Function to perform quicksort using the leftmost element as the pivot
def quickSortleftpivot(arr):
    return quickSortleftpivotHelper(arr, 0, len(arr) - 1)

def shell_sort(arr):
    length = len(arr)
    #sorting the array using the gap and insertion sort
    k=length//23
    while k>=0:
        gap = (4**(k+1))+(3*(2**k))+1 #generating the gap using Segwick's formula
        if gap>length:
            k-=1
            continue
        tmp = insertionSort(arr[0:length:gap])
        for j in range(len(tmp)):
            arr[j*gap]=tmp[j]
        k-=1
    arr = insertionSort(arr[0:length:1])
    return arr

def sort_using_algorithm(data, algorithm):
    print("before sorting",data)
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
