"""
To run this file issue this command:
python3 HelloWorld.py

Python as a interpreted language executes code directly without a separate compilation step, 
translating and running the source code on-the-fly during execution.
"""
import sys
from HelloWorld import HelloWorld


# Checks if the Python script is being run as the main program (not imported as a module)
def shell_sort(arr):
    length = len(arr)
    gap = [1]
    k=0
    while True:
        tmp=(4**(k+1))+(3*(2**k))+1
        if tmp<=length:
            gap.append(tmp)
        else:
            break
        k+=1
    for i in range(len(gap)-1,-1,-1):
        for j in range(0,length,gap[i]):
            key=arr[j]
            k=j-gap[i]
            while k>=0 and arr[k]>key:
                arr[k+gap[i]]=arr[k]
                k-=gap[i]
            arr[k+gap[i]]=key
    return arr
def heapify(arr,index,sorting,indexstop):
        if sorting==False:
            if indexstop<=(2*index)+1:
                return 0
        else:
            if indexstop<(2*index)+2:
                return 0
        if arr[(2*index)+1]>=arr[(2*index)+2] or (sorting==True and indexstop<=(2*index)+2):
            if arr[index]<arr[(2*index)+1] and indexstop>(2*index)+1:
                arr[index],arr[(2*index)+1]=arr[(2*index)+1],arr[index]
                heapify(arr,(2*index)+1,sorting,indexstop)
        else:
            if arr[index]<arr[(2*index)+2] and indexstop>(2*index)+2:
                arr[index],arr[(2*index)+2]=arr[(2*index)+2],arr[index]
                heapify(arr,(2*index)+2,sorting,indexstop)

def heap_sort(arr):
    length=len(arr)
    for i in range(int(length//2)-1,-1,-1):
        if arr[(2*i)+1]>=arr[(2*i)+2]:
            arr[i],arr[(2*i)+1]=arr[(2*i)+1],arr[i]

        else:
            arr[i],arr[(2*i)+2]=arr[(2*i)+2],arr[i]
    for i in range(length-1):
        arr[0],arr[length-i]=arr[length-i],arr[0]
        heapify(arr,0,True,length-1)
    return arr

def insertionSort(arr):
    length = len(arr)
    if length <= 1:
        return
    for i in range(1, length):
        key = arr[i]
        j = i - 1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key

def selectionSort(arr):
    length = len(arr)
    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            if arr[j] < arr[min_index]:
                min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]

def divqSort():
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

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
