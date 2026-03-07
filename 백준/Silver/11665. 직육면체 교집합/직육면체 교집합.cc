#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;
    int max_x1 = 0, max_y1 = 0, max_z1 = 0;
    int min_x2 = 1001, min_y2 = 1001, min_z2 = 1001;
    while (N--) {
        int x1, y1, z1, x2, y2, z2;
        cin >> x1 >> y1 >> z1 >> x2 >> y2 >> z2;
        max_x1 = max(x1, max_x1);
        max_y1 = max(y1, max_y1);
        max_z1 = max(z1, max_z1);
        min_x2 = min(x2, min_x2);
        min_y2 = min(y2, min_y2);
        min_z2 = min(z2, min_z2);
    }
    int diff_x = min_x2 - max_x1, diff_y = min_y2 - max_y1, diff_z = min_z2 - max_z1;
    if (diff_x > 0 && diff_y > 0 && diff_z > 0) cout << diff_x * diff_y * diff_z;
    else cout << 0;
    return 0;
}