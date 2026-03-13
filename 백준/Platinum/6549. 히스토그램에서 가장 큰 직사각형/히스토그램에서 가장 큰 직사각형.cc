#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

vector<int> histogram;
vector<int> tree;

void init(int node, int start, int end) {
    if (start == end) {
        tree[node] = start;
        return;
    }
    int mid = (start + end) / 2;
    init(node * 2, start, mid);
    init(node * 2 + 1, mid + 1, end);

    if (histogram[tree[node * 2]] <= histogram[tree[node * 2 + 1]]) tree[node] = tree[node * 2];
    else tree[node] = tree[node * 2 + 1];
}

int query(int node, int start, int end, int left, int right) {
    if (left > end || right < start) return -1;
    if (left <= start && end <= right) return tree[node];
    int mid = (start + end) / 2;
    int m1 = query(node * 2, start, mid, left, right);
    int m2 = query(node * 2 + 1, mid + 1, end, left, right);

    if (m1 == -1) return m2;
    else if (m2 == -1) return m1;
    else return (histogram[m1] <= histogram[m2]) ? m1 : m2;
}

long long solve(int N, int left, int right) {
    int m = query(1, 0, N - 1, left, right);
    long long area = (long long)histogram[m] * (long long)(right - left + 1);

    if (left <= m - 1) {
        area = max(area, solve(N, left, m - 1));
    }
    if (m + 1 <= right) {
        area = max(area, solve(N, m + 1, right));
    }
    return area;
}

int main() {
    while (true) {
        int N;
        cin >> N;
        if (N == 0) break;

        histogram.clear();
        histogram.resize(N);
        for (int i = 0; i < N; i++) cin >> histogram[i];

        int h = (int)ceil(log2(N));
        int tree_size = (1 << (h + 1));
        tree.assign(tree_size, 0);

        init(1, 0, N - 1);
        
        cout << solve(N, 0, N - 1) << "\n";
    }

    return 0;
}