#include <iostream>

using namespace std;

int main() {
    int K;
    cin >> K;

    int choco = 1;
    while (choco < K) {
        choco <<= 1;
    }
    cout << choco << " ";

    int cnt = 0;
    int temp_choco = choco;
    while (K > 0) {
        if (K >= temp_choco) {
            K -= temp_choco;
        } else {
            temp_choco /= 2;
            cnt++;
        }
    }
    cout << cnt;

    return 0;
}