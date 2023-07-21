import random

def main():
    NUMBER_OF_ELEMENTS = 10
    list = []

    for i in range(NUMBER_OF_ELEMENTS):
        number = random.randint(0, 100)
        list.append(number)

    print('List before sorted: ', list)
    print('List after selection sort ASC: ', insertionSort_ASC(list))
    print('List after selection sort DESC: ', insertionSort_DESC(list))

def insertionSort_ASC(list):
    for i in range(1, len(list)):
        j, fixed = i-1, list[i]
        while j >= 0 and list[j] > fixed:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = fixed
    
    return list


def insertionSort_DESC(list):
    for i in range(1, len(list)):
        j, fixed = i-1, list[i]
        while j >= 0 and list[j] < fixed:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = fixed

    return list

if __name__ == '__main__':
    main()