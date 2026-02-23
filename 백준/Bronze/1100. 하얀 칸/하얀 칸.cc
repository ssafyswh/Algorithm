#include <iostream>
#include <string>

using namespace std;

int main() {
    int result = 0;
    for (int i = 0; i < 8; i++) {
        string row;
        cin >> row;
        for (int j = 0; j < 8; j++) {
            if (row[j] != 'F') continue;
            if (i % 2 == 0) {
                if (j % 2 == 0) result++;
            } else {
                if (j % 2 == 1) result++;
            }
        }
    }
    cout << result;
}