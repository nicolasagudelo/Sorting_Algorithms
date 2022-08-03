def insertion_sort(list, ascending = True):
    for step in range(1, len(list)):
        key = list[step]

        for index in range(step-1, -1, -1):
            if ascending:
                if list[index] > key:
                    list[index + 1], list[index] = list[index], key
            else:
                if list[index] < key:
                    list[index + 1], list[index] = list[index], key

unordered_list = [9, 5, 1, 4, 3]

insertion_sort(unordered_list)

print(unordered_list)

insertion_sort(unordered_list, False)

print(unordered_list)