import random

def main():
    NUMBER_OF_ELEMENTS = 10
    list = []

    for i in range(NUMBER_OF_ELEMENTS):
        number = random.randint(0, 100)
        list.append(number)

    print('List before sorted: ', list)
    print('List after selection sort ASC: ', mergeSort_ASC(list))
    print('List after selection sort DESC: ', mergeSort_DESC(list))

def mergeSort_ASC(list):
    if len(list) > 1:
        mid = len(list) // 2
        left_list = list[:mid]
        right_list = list[mid:]

        mergeSort_ASC(left_list)
        mergeSort_ASC(right_list)

        left_index = 0
        right_index = 0
        merge_index = 0

        while right_index < len(right_list) and left_index < len(left_list):
            if right_list[right_index] < left_list[left_index]:
                list[merge_index] = right_list[right_index]
                right_index += 1
            else:
                list[merge_index] = left_list[left_index]
                left_index += 1
            merge_index += 1

        while right_index < len(right_list):
            list[merge_index] = right_list[right_index]
            right_index += 1
            merge_index += 1

        while left_index < len(left_list):
            list[merge_index] = left_list[left_index]
            left_index += 1
            merge_index += 1

    return list

def mergeSort_DESC(list):
    if len(list) > 1:
        mid = len(list) // 2
        left_list = list[:mid]
        right_list = list[mid:]

        mergeSort_DESC(left_list)
        mergeSort_DESC(right_list)

        left_index = 0
        right_index = 0
        merge_index = 0

        while right_index < len(right_list) and left_index < len(left_list):
            if right_list[right_index] > left_list[left_index]:
                list[merge_index] = right_list[right_index]
                right_index += 1
            else:
                list[merge_index] = left_list[left_index]
                left_index += 1
            merge_index += 1

        while right_index < len(right_list):
            list[merge_index] = right_list[right_index]
            right_index += 1
            merge_index += 1

        while left_index < len(left_list):
            list[merge_index] = left_list[left_index]
            left_index += 1
            merge_index += 1

    return list

if __name__ == '__main__':
    main()
