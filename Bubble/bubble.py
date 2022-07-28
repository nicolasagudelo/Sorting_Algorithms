from re import A


def bubble_sort(lst, ascending = True):
    # print(lst)
    unordered = True
    while unordered:
        unordered = False
        for index in range(len(lst) - 1):
            if lst[index] > lst[index + 1] and ascending == True:
                temp = lst[index]
                lst[index] = lst[index + 1]
                lst[index + 1 ] = temp
                unordered = True
            if lst[index] < lst[index + 1] and ascending == False:
                temp = lst[index]
                lst[index] = lst[index + 1]
                lst[index + 1 ] = temp
                unordered = True
        # print(lst)

    return lst

print(bubble_sort([5,2,9,1,5]))
print(bubble_sort([5,2,9,1,5], False))
print(bubble_sort([3,5,4,6,2,1]))
print(bubble_sort([3,5,4,6,2,1], False))
