# python3

def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    BASE = 31
    PRIME = 10 ** 9 + 7
    BASE_POW_PATTERN = BASE ** (len(pattern) - 1)

    def get_char_to_idx(char):
        return ord(char) - ord('a')

    def calculate_pattern_hash(_pattern):
        _pattern_hash = 0
        for c in _pattern:
            _pattern_hash = (_pattern_hash * BASE + get_char_to_idx(c)) % PRIME
        return _pattern_hash

    answer = []
    start, end = 0, 0
    window_hash = 0
    pattern_hash = calculate_pattern_hash(pattern)
    while end < len(text):
        window_hash = (window_hash * BASE + get_char_to_idx(text[end])) % PRIME
        if end - start + 1 == len(pattern):
            if pattern_hash == window_hash and text[start:end + 1] == pattern:
                answer.append(start)
            window_hash -= get_char_to_idx(text[start]) * BASE_POW_PATTERN
            start += 1
        end += 1
    return answer

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
