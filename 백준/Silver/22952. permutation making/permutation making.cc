#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;

    cout << N << " ";
    for (int i = 1; i <= (N - 1) / 2; i++) {
        cout << i << " " << N - i << " ";
    }
    if (N > 1 && N % 2 == 0) {
        cout << N / 2;
    }
    return 0;
}