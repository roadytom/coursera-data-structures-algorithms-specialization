# python3

import sys


class PolynomialHasher:
    def __init__(self, string, mod=10 ** 9 + 7, base=31, match=None):
        self.length = len(string)
        self.string = string
        self.mod = mod
        self.base = base
        self.prefix_hashes = [0] * (self.length + 1)
        self.powers = [1] * (self.length + 1)
        self._initialize_powers()
        self._initialize_prefix_hashes()
        self.answer_set = set()
        if match:
            self.match = match
            self._initialize_set()

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
        return ord(ch)

    def is_exist(self, param):
        return param in self.answer_set

    def _initialize_set(self):
        for i in range(self.length - self.match + 1):
            self.answer_set.add(self.get_hash(i, i + self.match))


def solve(k, text, pattern):
    result = []
    text_length = len(text)
    pattern_length = len(pattern)
    required_match = pattern_length - k

    text_hasher = PolynomialHasher(text)
    pattern_hasher = PolynomialHasher(pattern, match=required_match)
    for i in range(text_length - pattern_length + 1):
        for start in range(i, i + k + 1):
            if pattern_hasher.is_exist(text_hasher.get_hash(i, i + required_match)):
                result.append(i)
                break
    return result


for line in sys.stdin.readlines():
    k, t, p = line.split()
    ans = solve(int(k), t, p)
    print(len(ans), *ans)
