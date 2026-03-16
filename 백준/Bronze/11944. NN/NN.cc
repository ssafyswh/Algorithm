#include <iostream>
#include <string>

using namespace std;

int main() {
    string N;
     int M;
    cin >> N >> M;
    int n = stoi(N);
    int len = N.length();
    if (n * len <= M) {
        for (int i = 0; i < n; i++) cout << N;
    } else {
        for (int i = 0; i < M / len; i++) cout << N;
        for (int i = 0; i < M % len; i++) cout << N[i];
    }
    return 0;
}