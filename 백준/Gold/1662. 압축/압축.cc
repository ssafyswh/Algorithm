#include <iostream>
#include <string>

using namespace std;

pair<int, int> solve(string S, int idx = 0) {
    int len = 0;
    while (idx < S.length()) {
        char now = S[idx];
        if (now == '(') {
            len -= 1;
            int k = S[idx - 1] - '0';
            idx ++;
            pair<int, int> sub = solve(S, idx);
            int sub_len = sub.first, sub_fin = sub.second;
            len += k * sub_len;
            idx = sub_fin + 1;
        } else if (now ==')') {
            return {len, idx};
        } else {len++; idx++;}
    }
    return {len, S.length()};
}

int main() {
    string S;
    cin >> S;
    cout << solve(S).first;
    return 0;
}