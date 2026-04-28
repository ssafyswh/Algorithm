r, c = map(int, input().split())
windows = [input() for _ in range(r)]
patterns = set()
window_r = 1
window_c = 1
while True:
    if windows[window_r + 1][window_c] == '#':
        break
    window_r += 1
while True:
    if windows[window_r][window_c + 1] == '#':
        break
    window_c += 1

for i in range((r - 1) // (window_r + 1)):
    for j in range((c - 1) // (window_c + 1)):
        pattern = tuple([windows[1 + i * (window_r + 1) + y][1 + j * (window_c + 1):(j + 1) * (window_c + 1)] for y in range(window_r)])
        if window_r == window_c: # must consider 90, 270
            pattern_90 = [''] * window_r
            pattern_270 = [''] * window_r
            for y in range(window_r):
                for x in range(window_c):
                    pattern_90[y] = pattern[x][y] + pattern_90[y]
                    pattern_270[y] += pattern[x][-(y + 1)]
            if tuple(pattern_90) in patterns or tuple(pattern_270) in patterns:
                continue
        pattern_180 = [''] * window_r
        for y in range(window_r):
            for x in range(window_c):
                pattern_180[-(y + 1)] = pattern[y][x] + pattern_180[-(y + 1)]
        if tuple(pattern_180) in patterns:
            continue

        patterns.add(pattern)

print(len(patterns))