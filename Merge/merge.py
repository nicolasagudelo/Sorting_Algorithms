def merge_sort(lst, ascending = True):
    if len(lst) > 1:
        middle = len(lst) // 2
        left_split = lst[:middle]
        right_split = lst[middle:]
        return merge(merge_sort (left_split, ascending), merge_sort (right_split, ascending), ascending)
    else:
        return lst

def merge(left, right, ascending):
    ordered_lst = []
    if ascending == True:
        while left and right:
            if left[0] < right [0]:
                ordered_lst.append(left.pop(0))
            else:
                ordered_lst.append(right.pop(0))
        if left:
            ordered_lst += left
        if right:
            ordered_lst += right

        return ordered_lst
    if ascending == False:
        while left and right:
            if left[0] < right [0]:
                ordered_lst.append(right.pop(0))
            else:
                ordered_lst.append(left.pop(0))
        if left:
            ordered_lst += left
        if right:
            ordered_lst += right

        return ordered_lst


    



print(merge_sort([5,2,9,1,5]))
print(merge_sort([5,2,9,1,5], False))
print(merge_sort([3,5,4,6,2,1]))
print(merge_sort([3,5,4,6,2,1], False))
print(merge_sort([2,6,3,5,1]))
