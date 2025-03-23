#!/usr/bin/python3

import sys
import threading
from collections import deque

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


def IsBinarySearchTreeInOrder(tree, nodes):
    if not tree:
        return True
    key = [0] * nodes
    left = [0] * nodes
    right = [0] * nodes
    for i in range(nodes):
        [a, b, c] = tree[i]
        key[i] = a
        left[i] = b
        right[i] = c

    result = []

    def in_order_traversal(idx):
        if idx == -1:
            return
        in_order_traversal(left[idx])
        result.append(key[idx])
        in_order_traversal(right[idx])

    in_order_traversal(0)
    return all(result[i] < result[i + 1] for i in range(len(result) - 1))


def IsBinarySearchTree(tree, nodes):
    if not tree:
        return True
    n = len(tree)
    key = [0] * n
    left = [0] * n
    right = [0] * n
    for i in range(n):
        [a, b, c] = tree[i]
        key[i] = a
        left[i] = b
        right[i] = c
    stack = deque([(0, float("-inf"), float("inf"), False)])
    while stack:
        idx, mn, mx, left_child = stack.pop()
        if key[idx] < mn or key[idx] > mx or (left_child and key[idx] == mx):
            return False
        if left[idx] != -1:
            stack.append((left[idx], mn, key[idx], True))
        if right[idx] != -1:
            stack.append((right[idx], key[idx], mx, False))

    return True


def main():
    nodes = int(input())
    tree = [None] * nodes
    for idx in range(nodes):
        a, b, c = map(int, input().split())
        tree[idx] = (a, b, c)
    if nodes == 0 or IsBinarySearchTree(tree, nodes):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
