from random import randint

def quicksort(list, ascending = True):
    result = []
    lenght = len(list)
    if lenght == 0:
        return
    if lenght == 1:
        return list        
    pivot_index = randint(0, lenght - 1)
    pivot = []
    pivot.append(list[pivot_index])
    greater_than = []
    lesser_than = []
    for index in range(lenght):
        if index == pivot_index:
            continue
        if list[index] > pivot[0]:
            greater_than.append(list[index])
        else:
            lesser_than.append(list[index])
    if ascending:
        if quicksort(lesser_than) is not None:
            result += quicksort(lesser_than)
        result += (pivot)
        if quicksort(greater_than) is not None:
            result += (quicksort(greater_than))
        return result
    else:
        if quicksort(greater_than, ascending) is not None:
            result += (quicksort(greater_than, ascending))
        result += (pivot)
        if quicksort(lesser_than, ascending) is not None:
            result += quicksort(lesser_than, ascending)
        return result

print(quicksort([3,2,1]))
print(quicksort([5,2,9,1,5]))
print(quicksort([5,2,9,1,5], False))
print(quicksort([3,5,4,6,2,1]))
print(quicksort([3,5,4,6,2,1], False))
print(quicksort([2,6,3,5,1]))