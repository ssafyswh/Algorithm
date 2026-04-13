#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
    long long H, W;
    int N;
    cin >> H >> W >> N;

    map<pair<int, int>, int> cnt;

    for (int i = 0; i < N; i++) {
        int r, c;
        cin >> r >> c;
        for (int dy = 0; dy < 3; dy++) {
            int start_r = r - dy;
            if (start_r < 1 || start_r > H - 2) continue;
            for (int dx = 0; dx < 3; dx++) {
                int start_c = c - dx;
                if (start_c < 1 || start_c > W - 2) continue;
                cnt[{start_r, start_c}]++;
            }
        }
    }
    vector<long long> result(10, 0);
    result[0] = (H - 2) * (W - 2);
    for (auto const& [p, count] : cnt) {
        result[count]++;
        result[0]--;
    }
    for (long long r : result) cout << r << "\n";
    return 0; 
}