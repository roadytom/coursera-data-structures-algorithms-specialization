# python3

import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')

BASE = 31
MOD1 = 10 ** 9 + 9
MOD2 = 10 ** 9 + 7

factors1 = []
factors2 = []


def initialize_prime_factors(length, mod):
    _factors = [1]
    for i in range(length + 1):
        _factors.append((_factors[-1] * BASE) % mod)
    return _factors


def build_hash_dict(string, possible_len, mod, f):
    hashes = {}
    hash = 0
    start, end = 0, 0
    while end < len(string):
        hash = (hash * BASE) % mod + get_char_to_idx(string[end])
        if end - start + 1 == possible_len:
            hashes[hash] = start
            hash = hash - (get_char_to_idx(string[start]) * f[end - start]) % mod
            start += 1
        end += 1
    return hashes


def get_char_to_idx(char):
    return ord(char) - ord('a') + 1


def get_equal_substring_idx_or_none(s, t, possible_len):
    s_dict1 = build_hash_dict(t, possible_len, MOD1, factors1)
    s_dict2 = build_hash_dict(t, possible_len, MOD2, factors2)
    hash1 = 0
    hash2 = 0
    start, end = 0, 0
    while end < len(s):
        hash1 = (hash1 * BASE) % MOD1 + get_char_to_idx(s[end])
        hash2 = (hash2 * BASE) % MOD2 + get_char_to_idx(s[end])

        if end - start + 1 == possible_len:
            if hash1 in s_dict1 and hash2 in s_dict2 and s_dict1[hash1] == s_dict2[hash2]:
                return start, s_dict1[hash1]
            hash1 = hash1 - (get_char_to_idx(s[start]) * factors1[end - start]) % MOD1
            hash2 = hash2 - (get_char_to_idx(s[start]) * factors2[end - start]) % MOD2
            start += 1
        end += 1
    return None


def solve(s, t):
    global factors1, factors2
    ans = Answer(0, 0, 0)
    left = 1
    right = min(len(s), len(t))
    factors1 = initialize_prime_factors(right, MOD1)
    factors2 = initialize_prime_factors(right, MOD2)
    while left <= right:
        possible_len = (left + right) // 2
        idxs = get_equal_substring_idx_or_none(s, t, possible_len)
        if idxs is not None:
            ans = Answer(*idxs, possible_len)
            left = possible_len + 1
        else:
            right = possible_len - 1
    return ans


for line in sys.stdin.readlines():
    s, t = line.split()
    ans = solve(s, t)
    print(ans.i, ans.j, ans.len)
