#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        vector<int> store(n);
        for (int i = 0; i < n; i++) cin >> store[i];
        sort(store.begin(), store.end());
        int result = 0;
        for (int i = 0; i < n - 1; i++) {
            result += 2 * (store[i + 1] - store[i]);
        }
        cout << result << "\n";
    }
    return 0;
}