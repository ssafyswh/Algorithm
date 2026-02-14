#include <iostream>

using namespace std;


int main() {
    int result = 0, now = 0;
    for (int i = 0; i < 10; i++) {
        int in, out;
        cin >> out >> in;
        now = now - out + in;
        result = max(result, now);
        result = min(result, 10000);
    }
    cout << result;
}