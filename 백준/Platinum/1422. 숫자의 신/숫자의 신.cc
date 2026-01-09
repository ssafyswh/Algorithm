#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int K, N;
    cin >> K >> N;
    vector<string> nums(K);
    int max_val = 0;
    for (int i = 0; i < K; i ++ ) {
        int num;
        cin >> num;
        if (max_val < num) max_val = num;
        string s_num = to_string(num);
        nums[i] = s_num;
    }
    string max_val_s = to_string(max_val);
    sort(nums.begin(), nums.end(), [](const string& a, const string& b) {
        return a + b > b + a;
    });
    bool flag = true;
    for (int i = 0; i < K; i++) {
        string num = nums[i];
        if (num == max_val_s && flag) {
            for (int i = 0; i < N - K + 1; i++) {
                cout << num;
            }
            flag = false;
        } else cout << num;
    }
    return 0;
}