#Shell Sort Algorithm

def shellSort(data, length):

    gap = length//2

    while gap > 0:
        for iIndex in range(gap, length):

            temp = data[iIndex]
            
            jIndex = iIndex

            while jIndex >= gap and data[jIndex - gap] > temp:
                data[jIndex] = data[jIndex - gap]

                jIndex -= gap

            data[jIndex] = temp

        gap //= 2

    print(data)



