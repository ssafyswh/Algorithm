#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

vector<int> cnt(10, 0);

int main() {
    string nums;
    cin >> nums;
    int sum = 0;
    for (char num : nums) {
        cnt[num - '0']++;
        sum += num -'0';
    }
    if (cnt[0] == 0 || sum % 3 != 0) cout << -1;
    else {
        for (int i = 9; i >= 0; i--) {
            while (cnt[i] > 0) {
                cout << i;
                cnt[i]--;
            }
        }
    }
    return 0;
}