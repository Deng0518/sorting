import random

def main():
    NUMBER_OF_ELEMENTS = 10
    list = []

    for i in range(NUMBER_OF_ELEMENTS):
        number = random.randint(0, 100)
        list.append(number)

    print('List before sorted: ', list)
    print('List after bubble sort ASC: ', bubbleSort_ASC(list))
    print('List after bubble sort DESC: ', bubbleSort_DESC(list))

def bubbleSort_ASC(list):
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                isSorted = False
    
    return list

def bubbleSort_DESC(list):
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(list)-1):
            if list[i] < list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                isSorted = False

    return list

if __name__ == '__main__':
    main() 
