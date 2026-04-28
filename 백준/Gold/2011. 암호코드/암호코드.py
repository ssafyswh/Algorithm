import sys
sys.setrecursionlimit(10**6)

def solve_decoding(S):
    S_len = len(S)
    if S_len == 0:
        return 0
    memo = {}

    def decode_count(pointer):
        if pointer == S_len:
            return 1

        if pointer in memo:
            return memo[pointer]

        if S[pointer] == '0':
            return 0

        count = 0
        count += decode_count(pointer + 1)

        if pointer < S_len - 1:

            two_digit = int(S[pointer:pointer + 2])

            if 10 <= two_digit <= 26:
                count += decode_count(pointer + 2)

        memo[pointer] = count
        return count % 1000000

    return decode_count(0) % 1000000

S = input()
print(solve_decoding(S))