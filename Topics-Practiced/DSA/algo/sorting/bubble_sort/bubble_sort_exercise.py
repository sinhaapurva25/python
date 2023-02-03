# https://github.com/sinhaapurva25/c/blob/main/data_structures/bubblesort.c
# https://www.geeksforgeeks.org/bubble-sort/

def swap(elements, a, b):
    if a != b:
        temp = elements[a]
        elements[a] = elements[b]
        elements[b] = temp


def bubble_sort(elements, key='transaction_amount'):
    for i in range(len(elements)):
        swapped = False
        for j in range(len(elements) - i - 1):
            if elements[j + 1][key] < elements[j][key]:
                swap(elements, j, j + 1)
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    elements = [{'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
                {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
                {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
                {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'}
               ]
    bubble_sort(elements, key='transaction_amount')
    [print(i) for i in elements]