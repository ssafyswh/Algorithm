#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> series(N);
    for (int i = 0; i < N; i++) {
        cin >> series[i];
    }

    sort(series.begin(), series.end());
    int target = 1;
    for (int i = 0; i < N; i++) {
        if (series[i] <= target) target += series[i];
        else break;
    }
    cout << target;
    return 0;
}