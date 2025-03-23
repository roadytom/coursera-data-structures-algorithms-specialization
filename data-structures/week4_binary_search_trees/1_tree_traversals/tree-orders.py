# python3

import sys
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []

        def in_order_traversal(idx):
            if idx == -1:
                return
            in_order_traversal(self.left[idx])
            self.result.append(self.key[idx])
            in_order_traversal(self.right[idx])

        in_order_traversal(0)
        return self.result

    def preOrder(self):
        self.result = []

        def pre_order_traversal(idx):
            if idx == -1:
                return
            self.result.append(self.key[idx])
            pre_order_traversal(self.left[idx])
            pre_order_traversal(self.right[idx])

        pre_order_traversal(0)
        return self.result

    def postOrder(self):
        self.result = []

        def post_order_traversal(idx):
            if idx == -1:
                return
            post_order_traversal(self.left[idx])
            post_order_traversal(self.right[idx])
            self.result.append(self.key[idx])

        post_order_traversal(0)
        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
