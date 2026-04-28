#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;
    int hours = 0;
    for (int i = 0; i < N; i++) {
        int t;
        cin >> t;
        hours += t + 8;
    }
    hours -= 8;
    cout << hours / 24 << " " << hours % 24;
    return 0;
}