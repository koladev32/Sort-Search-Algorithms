#Bucket Sort Algorithm

def bucketSort(data):
    bucket = []

    for iIndex in range(len(data)):
        bucket.append([])

    for jIndex in data:
        index_bucket = int(10 * jIndex)
        bucket[index_bucket].append(jIndex)
        print(bucket)

    for iIndex in range(len(data)):
        bucket[iIndex] = sorted(bucket[iIndex])

        kIndex = 0
        
        for iIndex in range(len(data)):

            for jIndex in range(len(bucket[iIndex])):
                data[kIndex] = bucket[iIndex][jIndex]
                kIndex += 1

    print(data)
