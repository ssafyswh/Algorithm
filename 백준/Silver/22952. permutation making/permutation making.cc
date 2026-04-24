#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;
    for (int i = 0; i < (N - 1) / 2; i++) cout << i + 1 << " " << N - i - 1 << " ";
    if (N % 2 == 0) cout << N / 2 << " ";
    cout << N;
    return 0;
}