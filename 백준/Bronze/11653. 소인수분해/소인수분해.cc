#include <iostream>

using namespace std;

int main() {
    int N; 
    cin >> N;
    while (N > 1) {
        int div = 2;
        while (div <= N) {
            if (N % div == 0) {
                N /= div;
                cout << div << endl;
                break;
            }
            div++;
        }
    }

    return 0;
}