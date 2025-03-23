#!/usr/bin/python3

import sys
import threading
from collections import deque

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 25)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
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
    stack = deque([(0, float("-inf"), float("inf"))])
    while stack:
        idx, mn, mx = stack.pop()
        if key[idx] <= mn or key[idx] >= mx:
            return False
        if left[idx] != -1:
            stack.append((left[idx], mn, key[idx]))
        if right[idx] != -1:
            stack.append((right[idx], key[idx], mx))

    return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
