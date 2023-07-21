import random

def main():
    NUMBER_OF_ELEMENTS = 10
    list = []

    for i in range(NUMBER_OF_ELEMENTS):
        number = random.randint(0, 100)
        list.append(number)

    print('List before sorted: ', list)
    quickSort(list, 0, len(list)-1)
    print('List after selection sort ASC: ', list)

def quickSort(list, left, right):
    if left < right:
        partition_pos = partition(list, left, right)
        quickSort(list, left, partition_pos-1)
        quickSort(list, partition_pos+1, right)

def partition(list, left, right):
    i = left
    j = right - 1
    pivot = list[right]

    while i < j:
        while i < right and list[i] < pivot:
            i += 1

        while j > left and list[j] > pivot:
            j -= 1

        if i < j:
            list[i], list[j] = list[j], list[i]

    if list[i] > pivot:
        list[i], list[right] = list[right], list[i]

    return i

if __name__ == '__main__':
    main()