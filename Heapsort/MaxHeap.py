class MaxHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    def add(self, element):
        self.count += 1
        print(f"Adding: {element} to {self.heap_list}")
        self.heap_list.append(element)
        self.heapify_up()

    def heapify_up(self):
        # print("Restoring heap properties")
        idx = self.count
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]
            if parent < child:
                print(f"swapping {parent} with {child}")
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child
            idx = self.parent_idx(idx)
        # print(f"Heap Restored {self.heap_list}")
    
    def heapify_down(self):
        idx = 1
        # print('Restoring heap properties')
        while self.child_present(idx):
            larger_child_idx = self.get_larger_child_idx(idx)
            parent = self.heap_list[idx]
            child = self.heap_list[larger_child_idx]

            if parent < child:
                self.heap_list[idx] = child
                self.heap_list[larger_child_idx] = parent
            idx = larger_child_idx
        # print(f'Heap restored! {self.heap_list}')

    def child_present(self, idx):
        if self.right_child_idx(idx) > self.count and self.left_child_idx(idx) > self.count:
            return False
        return True

    def get_larger_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            # print('There is only a left child')
            return self.left_child_idx(idx)
        else:
            right_child = self.heap_list[self.right_child_idx(idx)]
            left_child = self.heap_list[self.left_child_idx(idx)]

            if left_child > right_child:
                # print('Left child is bigger')
                return self.left_child_idx(idx)
            else:
                # print('Right child is bigger')
                return self.right_child_idx(idx)

    def retrieve_max(self):
        if self.count == 0:
            print("No items in the heap")
            return None
        max_val = self.heap_list[1]
        print(f'removing {max_val} from {self.heap_list}')
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        print(f'Last element moved to first: {self.heap_list}')
        self.heapify_down()
        return max_val
    
        



# # Testing Max Heap.
# max_heap = MaxHeap()

# random_nums = [randrange(1, 101) for n in range(6)]
# for el in random_nums:
#     max_heap.add(el)

# print(max_heap.heap_list)
# print(max_heap.heap_list[max_heap.left_child_idx(1)])
# print(max_heap.heap_list[max_heap.left_child_idx(6)])

