#include <iostream>
#include <string>

using namespace std;

int main() {
    string L, R;
    cin >> L >> R;
    if (L.length() != R.length()) cout << 0;
    else {
        int count = 0;
        for (int i = 0; i < L.length(); i++) {
            if (L[i] == R[i]) {
                if (L[i] == '8') count++;
            }
            else break;
        }
        cout << count;
    }

    return 0;   
}