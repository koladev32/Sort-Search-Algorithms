#Linear Seach Algorithm

def linearSearch(data, number):
    found = False

    for index in range(0, len(data)):
        if (data[index] == number):
            found = True
            break
    if found:
        print("Element is present in the array", index)
    else:
        print("Element is not present in the array.")


