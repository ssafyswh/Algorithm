#include <iostream>
#include <string>

using namespace std;

int main() {
    int N;
    cin >> N;
    int coeff;
    cin >> coeff;
    int result = 1;
    for (int i = 0; i < N; i++) {
        int coeff;
        cin >> coeff;
        if (coeff > 0) {
            string s = to_string(coeff);
            result += (1 + s.length());
        }
        if (i < N - 1) {
            result += 2;
        }
    }
    result += 1;
    cout << result;
    return 0;
}