#include <iostream>
#include <string>

using namespace std;

int N;

bool is_good(string s) {
    int len = s.length();
    for (int i = 1; i <= len / 2; i++) {
        string front = s.substr(len - i, i);
        string rear = s.substr(len - 2 * i, i);
        if (front == rear) return false;
    }
    return true;
}

bool finished = false;

void solve(string s) {
    if (finished) return;

    if (s.length() == N) {
        cout << s;
        finished = true;
        return;
    }

    for (int i = 1; i <= 3; i++) {
        string next_s = s + to_string(i);
        if (is_good(next_s)) {
            solve(next_s);
        }
    }
}

int main() {
    cin >> N;
    solve("");
    return 0;
}