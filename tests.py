from QuickSort.quicksort import quickSort as qk
from MergeSort.mergesort import mergeSort as ms
from InsertionSort.insertionsort import insertionSort as inS
from BubbleSort.bubblesort import bubbleSort as bs
table = [9,7,10,3,4,6,5,4,1,2,0,8]
print("TESTING SORTING ALGORITHMS ON ", table)

print("\nQuick Sort \n")
qk(table, 0 , len(table)-1)
print("\nMerge Sort \n")
ms(table)
print("\nInsertion Sort\n")
inS(table)
print("\nBubble Sort\n")
bs(table)
