def selection_sort(list, ascending = True):
    if ascending:
        for step in range(len(list) - 1):
            min_idx = step
            for index in range(step+1, len(list)):
                if list[index] < list[min_idx]:
                    min_idx = index
            list[step], list[min_idx] = list[min_idx], list[step]
        return
    else:
        for step in range(len(list) - 1):
            max_idx = step
            for index in range(step+1, len(list)):
                if list[index] > list[max_idx]:
                    max_idx = index
            list[step], list[max_idx] = list[max_idx], list[step]
        return


unsorted_list = [20, 12, 10, 15, 2]
print('BEFORE:',unsorted_list)
selection_sort(unsorted_list)
print('AFTER:', unsorted_list)

selection_sort(unsorted_list, False)
print('INVERSE ORDER:', unsorted_list)
