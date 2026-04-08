#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;
    int result = 1;
    long long num;
    cin >> num;
    for (int i = 1; i < N; i++) {
        long long nxt;
        cin >> nxt;
        if (num >= nxt) {
            result = 0;
            break;
        }
        num = nxt;
    }
    cout << result;
    return 0;
}