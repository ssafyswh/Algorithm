#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);
        int N;
        long long result = 0;
        cin >> N;
        int stock[N] = {0};
        for (int i = 0; i < N; i++) {
            cin >> stock[i];
        }
        int highest = 0;
        for (int i = N - 1; i >= 0; i--) {
            int price = stock[i];
            if (highest < price) highest = price;
            else result += highest - price;
        }
        cout << result << "\n";
    }
    return 0;
}