#include <iostream>
#include <vector>
#include <map>

using namespace std;

int N;
vector<int> nums;
vector<int> oper(4);

int min_val = 1000000001;
int max_val = -1000000001;

void solve(int step, int calc) {
    if (step == N - 1) {
        min_val = min(min_val, calc);
        max_val = max(max_val, calc);
        return;
    }
    if (oper[0]) {
        oper[0]--;
        solve(step + 1, calc + nums[step + 1]);
        oper[0]++;
    }
    if (oper[1]) {
        oper[1]--;
        solve(step + 1, calc - nums[step + 1]);
        oper[1]++;
    }
    if (oper[2]) {
        oper[2]--;
        solve(step + 1, calc * nums[step + 1]);
        oper[2]++;
    }
    if (oper[3]) {
        oper[3]--;
        solve(step + 1, calc / nums[step + 1]);
        oper[3]++;
    }
}

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        int num;
        cin >> num;
        nums.push_back(num);
    }
    for (int i = 0; i < 4; i++) cin >> oper[i];
    solve (0, nums[0]);
    cout << max_val << "\n" << min_val;
    return 0;
}