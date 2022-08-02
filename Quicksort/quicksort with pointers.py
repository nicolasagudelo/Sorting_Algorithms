from random import randint, shuffle

def quicksort(list, start, end, ascending = True):
    if start >= end:
        return
    pivot_index = randint(start, end)
    pivot = list[pivot_index]

    list[end], list[pivot_index] = list[pivot_index], list[end]
    if ascending:
        less_than_pointer = start

        for index in range(start, end):
            if list[index] < pivot:
                list[index], list[less_than_pointer] = list[less_than_pointer], list[index]
                less_than_pointer += 1

        list[end], list[less_than_pointer] = list[less_than_pointer], list[end]

        quicksort(list, start, less_than_pointer - 1)
        quicksort(list, less_than_pointer + 1, end)
    else:
        greater_than_pointer = start

        for index in range(start, end):
            if list[index] > pivot:
                list[index], list[greater_than_pointer] = list[greater_than_pointer], list[index]
                greater_than_pointer += 1

        list[end], list[greater_than_pointer] = list[greater_than_pointer], list[end]

        quicksort(list, start, greater_than_pointer - 1, ascending)
        quicksort(list, greater_than_pointer + 1, end, ascending)

unsorted_list = [3,7,12,24,36,42]

shuffle(unsorted_list)
print(unsorted_list)
# use quicksort to sort the list, then print it out!
quicksort(unsorted_list, 0, len(unsorted_list) - 1)
print(unsorted_list)

quicksort(unsorted_list, 0, len(unsorted_list) - 1, False)
print(unsorted_list)