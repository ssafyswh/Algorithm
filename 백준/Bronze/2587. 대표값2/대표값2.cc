#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<int> nums;
    int sum = 0;
    for (int i = 0; i < 5; i ++) {
        int num;
        cin >> num;
        nums.push_back(num);
        sum += num;
    }
    sort(nums.begin(), nums.end());
    cout << sum / 5 << "\n" << nums[2];
}