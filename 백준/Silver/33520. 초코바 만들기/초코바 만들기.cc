#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;
    long long width = 0, height = 0;
    for (int i = 0; i < N; i++) {
        long long a, b;
        cin >> a >> b;
        if (a > b) swap(a, b);
        width = max(width, a);
        height = max(height, b);
    }
    cout << width * height;
    return 0;
}