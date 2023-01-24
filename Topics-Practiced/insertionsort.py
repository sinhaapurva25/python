'''
check the same C implementation at https://github.com/sinhaapurva25/c/blob/main/data_structures/insertionsort.c
'''

def insertionSort(array):
    print(array,'\n')
    k = 0 # total number of swaps
    for step in range(1, len(array)):
        min = array[step]
        print(step,min)
        j = step - 1
        
        # Compare min with each element on the left of it until an element smaller than it is found
        # For descending order, change min<array[j] to min>array[j].        
        
        while min < array[j] and j >= 0:
            print(j, array)
            array[j + 1] = array[j]
            j = j - 1
            k += 1
        
        # Place min at after the element just smaller than it.
        array[j + 1] = min
        print(array)
        print(sep='\n')
    print(k)

# data = [9, 5, 1, 4, 3]
data = [9, 8, 7, 6, 5, 4, 3, 2]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)