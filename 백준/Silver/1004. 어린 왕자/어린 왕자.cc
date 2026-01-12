#include <iostream>
#include <unordered_set>
#include <algorithm>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        int n;
        cin >> n;
        unordered_set<int> A, B;
        for (int i = 0; i < n; i ++) {
            int x, y, r;
            cin >> x >> y >> r;
            int dx1 = x1 - x, dx2 = x2 - x, dy1 = y1 - y, dy2 = y2 - y;
            if (dx1 * dx1 + dy1 * dy1 < r * r) A.insert(i);
            if (dx2 * dx2 + dy2 * dy2 < r * r) B.insert(i);
        }
        unordered_set<int> result;
        for (int a : A) {
            if (B.find(a) == B.end()) result.insert(a);
            
        }
        for (int b : B) {
            if (A.find(b) == A.end()) result.insert(b);
        }
        cout << result.size() << "\n";
    }
    return 0;
}