# python3

class HeapQ:
    def __init__(self):
        self.swaps = []
        self.data = None

    def heapify_returning_swaps(self, data):
        self.data = data
        for i in range(self.get_last_non_leaf_idx(), -1, -1):
            self.sift_down(i)
        return self.swaps

    def get_last_non_leaf_idx(self):
        return len(self.data) // 2 - 1

    def heappush(self, element):
        self.data.append(element)
        self.sift_up(len(self.data) - 1)

    def heappop(self):
        if not self.data:
            raise Exception("Heap is empty")
        popped = self.data[0]
        self.swap(0, -1)
        self.data.pop()
        self.sift_down(0)
        return popped

    def sift_down(self, idx):
        while self.has_child(idx) and self.larger_than_children(idx):
            max_child_idx = self.get_left_child_idx(idx) if self.get_left_child(idx) < self.get_right_child(
                idx) else self.get_right_child_idx(idx)
            self.swap(idx, max_child_idx)
            self.sift_down(max_child_idx)

    def swap(self, idx1, idx2):
        if idx1 == idx2:
            return
        self.swaps.append((idx1, idx2))
        self.data[idx1], self.data[idx2] = self.data[idx2], self.data[idx1]

    def get_left_child(self, idx):
        return self.data[self.get_left_child_idx(idx)]

    def get_right_child(self, idx):
        return self.data[self.get_right_child_idx(idx)]

    def sift_up(self, idx):
        while idx > 0 and self.data[idx] < self.get_parent(idx):
            parent_idx = self.get_parent_idx(idx)
            self.swap(parent_idx, idx)
            idx = parent_idx

    def has_child(self, idx):
        return self.get_left_child_idx(idx) < len(self.data)

    def larger_than_children(self, idx):
        return self.data[idx] > self.get_left_child(idx) or self.data[idx] > self.get_right_child(idx)

    def get_parent_idx(self, idx):
        return (idx - 1) // 2

    def get_left_child_idx(self, idx):
        return 2 * idx + 1

    def get_right_child_idx(self, idx):
        return 2 * idx + 2

    def get_parent(self, idx):
        return self.data[self.get_parent_idx(idx)]


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    heapq = HeapQ()
    return heapq.heapify_returning_swaps(data)


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
