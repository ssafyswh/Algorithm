import sys
input = sys.stdin.readline

def solve():
    n = int(input())

    ips = []
    for _ in range(n):
        ip = [*map(int, input().split('.'))]
        ip_int = (ip[0] << 24) + (ip[1] << 16) + (ip[2] << 8) + ip[3]
        ips.append(ip_int)

    common_bits = 32
    first_ip = ips[0]

    for i in range(1, n):
        diff = first_ip ^ ips[i]
        if diff == 0:
            current_common = 32
        else:
            diff_len = diff.bit_length()
            current_common = 32 - diff_len

        common_bits = min(common_bits, current_common)

    if common_bits == 0:
        net_mask_int = 0
    else:
        net_mask_int = (0xFFFFFFFF << (32 - common_bits)) & 0xFFFFFFFF
    net_addr_int = first_ip & net_mask_int

    def int_to_ip(n):
        return f"{(n >> 24) & 0xFF}.{(n >> 16) & 0xFF}.{(n >> 8) & 0xFF}.{n & 0xFF}"

    print(int_to_ip(net_addr_int))
    print(int_to_ip(net_mask_int))


solve()