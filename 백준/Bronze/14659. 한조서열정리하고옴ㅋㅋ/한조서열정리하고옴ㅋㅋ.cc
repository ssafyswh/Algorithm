#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    int result = 0, height = 0, cnt = 0;
    for (int i = 0; i < n; i++) {
        int hill;
        cin >> hill;
        if (height < hill) {
            height = hill;
            result = max(result, cnt);
            cnt = 0;
            continue;
        } else if (height > hill) {
            cnt++;
        }
    }
    result = max(result, cnt);
    cout << result;
    return 0;
}