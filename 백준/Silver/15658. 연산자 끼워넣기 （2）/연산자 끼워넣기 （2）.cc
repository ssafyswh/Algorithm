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
    for (int i = 0; i < 4; i++) {
        if (oper[i]) {
            int nxt_num = nums[step + 1];
            int nxt_calc;
            if (i == 0) nxt_calc = calc + nxt_num;
            else if (i == 1) nxt_calc = calc - nxt_num;
            else if (i == 2) nxt_calc = calc * nxt_num;
            else if (i == 3) nxt_calc = calc / nxt_num;
            oper[i]--;
            solve(step + 1, nxt_calc);
            oper[i]++;
        }
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