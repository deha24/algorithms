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

def heap_sort(arr):
    length=len(arr)
    for i in range(int(length//2)-1,-1,-1):
        if arr[(2*i)+1]>=arr[(2*i)+2]:
            arr[i],arr[(2*i)+1]=arr[(2*i)+1],arr[i]

        else:
            arr[i],arr[(2*i)+2]=arr[(2*i)+2],arr[i]
