#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;


pair<int, int> solve(string command, int N, int L) {
    unordered_map<int, int> cnt1(0);
    
    int pos1 = 1;
    cnt1[1] = 1;
    
    for (char d : command) {
        if (d == 'L') {
            pos1 = max(1, pos1 - 1);
        } else {
            pos1 = min(N, pos1 + 1);
        }
        cnt1[pos1]++;
    }

    if (cnt1[pos1] == 1) return {1, pos1};

    unordered_map<int, int> cnt2(0);
    int pos2 = N;
    cnt2[N] = 1;

    for (char d : command) {
        if (d == 'L') {
            pos2 = max(1, pos2 - 1);
        } else {
            pos2 = min(N, pos2 + 1);
        }
        cnt2[pos2]++;
    }
    if (cnt2[pos2] == 1) return {N, pos2};

    return {-1, -1};
}

int main() {
    int N, L;
    string command;
    cin >> N >> L >> command;
    pair<int, int> result = solve(command, N, L);
    if (result.first == -1) cout << "DEFEAT";
    else cout << "WIN\n" << result.first << " " << result.second;
    return 0;
}