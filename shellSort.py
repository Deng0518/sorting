import random

def main():
    NUMBER_OF_ELEMENTS = 10
    list = []
    gap = [5, 2, 1]

    for i in range(NUMBER_OF_ELEMENTS):
        number = random.randint(0, 100)
        list.append(number)

    print('List before sorted: ', list)
    print('List after selection sort ASC: ', shellSort_ASC(list, gap))
   # print('List after selection sort DESC: ', shellSort_DESC(list, gap))


def shellSort_ASC(list, gap):
    for current_gap in gap:
        for i in range(current_gap, len(list)):
            temp = list[i]
            j = i
            while j >= 0 and j - current_gap >= 0 and list[j-current_gap] > temp:
                list[j] = list[j-current_gap]
                j -= current_gap
            list[j] = temp

    return list

if __name__ == '__main__':
    main()