from MaxHeap import MaxHeap
from random import randrange

# create a heapsort function

def heapsort(lst, ascending = True):
    # create an empty list
    sort = []
    # make an instance of MaxHeap
    max_heap = MaxHeap()
    # add values from lst to max_heap
    for el in lst:
        max_heap.add(el)
    # print the heap list
    print(max_heap.heap_list)
    while max_heap.count > 0:
        if ascending == True:
            sort.insert(0, max_heap.retrieve_max())
        else:
            sort.append(max_heap.retrieve_max())

    return sort


my_list = [randrange(1, 50, 1) for i in range(6)]
sorted_list = heapsort(my_list)
inverse_list = heapsort(my_list, False)

print(sorted_list)
print(inverse_list)
