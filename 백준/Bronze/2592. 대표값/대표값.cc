#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
    unordered_map<int, int> cnt;
    int sum = 0;
    int mode = 0, mode_cnt = 0;
    for (int i = 0; i < 10; i++) {
        int num;
        cin >> num;
        sum += num;
        cnt[num]++;
        if (cnt[num] > mode_cnt) {
            mode = num;
            mode_cnt = cnt[num];
        }
    }
    cout << sum / 10 << "\n" << mode;
    return 0;
}