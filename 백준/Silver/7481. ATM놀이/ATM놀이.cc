#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int a, b, S;
        cin >> a >> b >> S;
        bool is_reversed = false;
        if (a < b) {
            swap(a, b);
            is_reversed = true;
        }
        int res_a = -1, res_b = -1;
        int max_a = S / a;
        for (int i = max_a; i >= 0 && (max_a - i) <= b; i--) {
            int remain = S - (i * a);
            if (remain % b == 0) {
                res_a = i;
                res_b = remain / b;
                break;
            } 
        }
        if (res_a == -1 || res_b == -1) cout << "Impossible" << "\n";
        else {
            if (is_reversed) cout << res_b << " " << res_a << "\n";
            else cout << res_a << " " << res_b << "\n";
        }
    }
    return 0;
}