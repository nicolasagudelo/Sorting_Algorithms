def bubble_sort(lst, ascending = True):
    for i in range(len(lst)):
        for index in range(len(lst) -i - 1):
            if lst[index] > lst[index + 1] and ascending == True:
                swap(lst, index, index + 1)
            if lst[index] < lst[index + 1] and ascending == False:
                swap(lst, index, index + 1)

    return lst

def swap(lst, i1, i2):
    temp = lst[i1]
    lst[i1] = lst[i2]
    lst[i2] = temp

print(bubble_sort([5,2,9,1,5]))
print(bubble_sort([5,2,9,1,5], False))
print(bubble_sort([3,5,4,6,2,1]))
print(bubble_sort([3,5,4,6,2,1], False))
print(bubble_sort([2,6,3,5,1]))
