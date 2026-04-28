#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        bool able = true;
        unsigned long long know = 0, impl = 0, think = 0, day = 0;
        for (int i = 0; i < N; i++) {
            unsigned long long a, b, c, p;
            cin >> a >> b >> c >> p;
            if (!able) continue;
            if (a > know) {
                day += (a - know);
                know = a;
            }
            if (b > impl) {
                day += (b - impl);
                impl = b;
            }
            if (c > think) {
                day += (c - think);
                think = c;
            }
            day++;
            if (day > p) able = false;
        }
        if (able) cout << "YES" << "\n";
        else cout << "NO" << "\n"; 
    }

    return 0;
}