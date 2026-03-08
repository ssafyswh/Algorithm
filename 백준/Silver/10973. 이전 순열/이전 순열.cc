#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool solve(vector<int>& a, int n) {
    int i = n - 1;
    while (i > 0 && a[i - 1] <= a[i]) i--;

    if (i <= 0) return false;
    int j = n - 1;

    while (a[j] >= a[i - 1]) j--;

    swap(a[i - 1], a[j]);
    reverse(a.begin() + i, a.end());
    return true;
}

int main() {
    int N;
    cin >> N;
    vector<int> series(N);
    for (int i = 0; i < N; i++) cin >> series[i];

    if (solve(series, N)) {
        for (int i = 0; i < N; i++) cout << series[i] << " ";
    } else cout << -1;
    return 0;
}