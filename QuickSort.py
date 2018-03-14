
"""
    快速排序Python实现（递归）
"""


def quickSort(arr, low, high):
    i = low
    j = high
    if i > j:
        return -1
    key = arr[i]
    while i < j:
        while i < j and arr[j] >= key:
            j = j - 1
        arr[i] = arr[j]
        while i < j and arr[i] <= key:
            i = i + 1
        arr[j] = arr[i]
    arr[i] = key
    quickSort(arr, low, i - 1)
    quickSort(arr, j + 1, high)
    return arr


def main():
    lis = [99, 25, 47, 1, 258, 96, 74, 15, 63, 84, 66]
    lists = quickSort(lis, 0, 10)
    print(lists)


if __name__ == '__main__':
    main()
