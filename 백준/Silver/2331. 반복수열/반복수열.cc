#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <cmath>

using namespace std;

int power(int a, int p) {
    int res = 1;
    for (int i = 0; i < p; i++) res *= a;
    return res;
}

int main() {
    int A, P;
    cin >> A >> P;
    unordered_set<int> nums;
    unordered_map<int, int> cnt;
    nums.insert(A);
    cnt[A]++;
    int num = A;
    while (true) {
        int new_num = 0;
        while (num > 0) {
            int digit = num % 10;
            new_num += power(digit, P);
            num /= 10;
        }
        cnt[new_num]++;
        nums.insert(new_num);
        if (cnt[new_num] >= 3) break;
        num = new_num;
    }
    int result = 0;
    for (int num : nums) {
        if (cnt[num] == 1) result++;
    }
    cout << result;
    return 0;
}