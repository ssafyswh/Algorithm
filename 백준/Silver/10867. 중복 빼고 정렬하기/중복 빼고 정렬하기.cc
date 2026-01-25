#include <iostream>
#include <set>

using namespace std;

int main() {
    set<int> nums;
    int N;
    cin >> N;
    while (N--) {
        int num;
        cin >> num;
        nums.insert(num);
    }
    for (int num : nums) cout << num << " ";
    return 0;
}