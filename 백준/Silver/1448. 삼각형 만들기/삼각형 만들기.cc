#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> straw(N);
    for (int i = 0; i < N; i++) {
        cin >> straw[i];
    }
    sort(straw.begin(), straw.end());
    int result = -1;
    for (int i = N - 3; i >= 0; i--) {
        if (straw[i] + straw[i + 1] > straw[i + 2]) {
            result = straw[i] + straw[i + 1] + straw[i + 2];
            break;
        }
    }
    cout << result;
    return 0;
}