"""
To run this file issue this command:
python3 HelloWorld.py

Python as a interpreted language executes code directly without a separate compilation step, 
translating and running the source code on-the-fly during execution.
"""

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
    for i in range(length):
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
        