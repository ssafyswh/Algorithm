#include <iostream>
#include <string>

using namespace std;

int main() {
    int N;
    cin >> N;

    for (int i = 0; i < 2 * N; i++) {
        string line(4 * N + 2, ' ');
        line[2 * N - 1 - i] = '*';

        if (i < N) {
            line[3 * N - i] = '*';
            line[3 * N + 2 + i] = '*';
        } else {
            line[N + 1 + i] = '*';
            line[5 * N + 1 - i] = '*';
        }

        cout << line << "\n";
    }

    return 0;
}