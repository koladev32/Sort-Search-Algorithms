
"""Quick Sort Algorithm"""

        
def quickSort(data, left, right):
    if right<= left:
        return 
    else:
        pivot = partition(data, left, right)
        quickSort(data, left, pivot - 1)
        quickSort(data, pivot + 1, right)

    return data
        
def partition(data, left, right):
    """This method chooses a pivot point that dertermines the left and right side of the sort"""
    pivot = data[left]
    leftIndex = left + 1
    rightIndex = right

    while True:
        while leftIndex <= rightIndex and data[leftIndex] <= pivot:
            leftIndex += 1
        while rightIndex >= leftIndex and data[rightIndex] >= pivot:
            rightIndex -= 1
        if rightIndex <= leftIndex:
            break
        data[leftIndex], data[rightIndex] = data[rightIndex], data [leftIndex]
        print(data)

    data[left], data[rightIndex] = data[rightIndex], data[left]
    print(data)

    return rightIndex

