#include <iostream>
#include <stack>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N;
        long long result = 0;
        cin >> N;
        stack<int> stock;
        for (int i = 0; i < N; i ++) {
            int price;
            cin >> price;
            stock.push(price);
        }
        int highest = 0;
        for (int i = 0; i < N; i ++) {
            if (highest < stock.top()) {
                highest = stock.top();
            } else {
                result += highest - stock.top();
            }
            stock.pop();
        }
        cout << result << "\n";
    }
    return 0;
}