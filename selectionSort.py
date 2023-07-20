import random

def main():
    NUMBER_OF_ELEMENTS = 10
    list = []

    for i in range(NUMBER_OF_ELEMENTS):
        number = random.randint(0, 100)
        list.append(number)

    print('List before sorted: ', list)
    print('List after selection sort ASC: ', selectionSort_ASC(list))
    print('List after selection sort DESC: ', selectionSort_DESC(list))

def selectionSort_ASC(list):
    for i in range(len(list)):
        minIdx = i
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                minIdx = j
        list[i], list[minIdx] = list[minIdx], list[i]

    return list

def selectionSort_DESC(list):
    for i in range(len(list)):
        minIdx = i
        for j in range(i+1, len(list)):
            if list[i] < list[j]:
                minIdx = j
        list[i], list[minIdx] = list[minIdx], list[i]

    return list

if __name__ == '__name__':
    main()