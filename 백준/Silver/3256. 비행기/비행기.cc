#include <iostream>
#include <vector>
#include <map>
#include <numeric>
#include <algorithm>
#include <string>

using namespace std;

int solve() {
    int N;
    if (!(cin >> N)) return 0;
    
    vector<int> P(N);
    for (int i = 0; i < N; ++i) {
        if (!(cin >> P[i])) return 0;
    }

    vector<int> Q(1001, -1);
    map<int, int> stayedTime;
    int resultTime = -1;

    auto hasCargo = [&Q]() {
        for (int val : Q) {
            if (val != -1) return true;
        }
        return false;
    };

    auto loop = [&](const string& condition) {
        int result = 0;
        
        while ((condition == "insert" && Q[0] != -1) || (condition == "move" && hasCargo())) {
            for (int j = 1000; j > 0; --j) {
                if (j == Q[j]) {
                    stayedTime[j]--;
                    if (stayedTime[j] == 0) {
                        stayedTime.erase(j);
                        Q[j] = -1;
                    }
                }

                if (Q[j] == -1 && Q[j - 1] != -1 && j <= Q[j - 1]) {
                    Q[j] = Q[j - 1];
                    Q[j - 1] = -1;
                    
                    if (j == Q[j]) {
                        stayedTime[j] = 5;
                    }
                }
            }
            result++;
        }
        return result;
    };

    for (int i = 0; i < N; ++i) {
        Q[0] = P[i];
        resultTime += loop("insert");
    }
        
    resultTime += loop("move");

    return resultTime;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cout << solve() << "\n";

    return 0;
}