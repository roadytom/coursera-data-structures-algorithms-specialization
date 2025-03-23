# python3

import sys


class PolynomialHasher:
    def __init__(self, string, mod=10 ** 9 + 7, base=31):
        self.length = len(string)
        self.string = string
        self.mod = mod
        self.base = base
        self.prefix_hashes = [0] * (self.length + 1)
        self.powers = [1] * (self.length + 1)
        self._initialize_powers()
        self._initialize_prefix_hashes()

    def _initialize_prefix_hashes(self):
        for i in range(1, self.length + 1):
            ch = self.string[i - 1]
            self.prefix_hashes[i] = ((self.prefix_hashes[i - 1] * self.base) % self.mod + self.char_to_idx(
                ch)) % self.mod

    def _initialize_powers(self):
        for i in range(1, self.length + 1):
            self.powers[i] = (self.powers[i - 1] * self.base) % self.mod

    def get_hash(self, start, end):
        return (self.prefix_hashes[end] - (
                self.prefix_hashes[start] * self.powers[end - start]) % self.mod + self.mod) % self.mod

    def check_substring_equality(self, start1, start2, l):
        return self.get_hash(start1, start1 + l) == self.get_hash(start2, start2 + l)

    def char_to_idx(self, ch):
        return ord(ch) - ord('a') + 1


s = sys.stdin.readline()
q = int(sys.stdin.readline())
hasher1 = PolynomialHasher(s, 10 ** 9 + 7, 31)
hasher2 = PolynomialHasher(s, 10 ** 9 + 9, 31)
for _ in range(q):
    a, b, l = map(int, sys.stdin.readline().split())
    print("Yes" if hasher1.check_substring_equality(a, b, l) and hasher2.check_substring_equality(a, b, l) else "No")
