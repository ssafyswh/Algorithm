#include <iostream>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;

double dist(double x1, double y1, double x2, double y2) {
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
}

int main() {
    double xA, yA, xB, yB, xC, yC;
    cin >> xA >> yA >> xB >> yB >> xC >> yC;

    if ((xB - xA) * (yC - yA) == (yB - yA) * (xC - xA)) {
        cout << -1.0 << "\n";
        return 0;
    }

    double ab = dist(xA, yA, xB, yB);
    double bc = dist(xB, yB, xC, yC);
    double ca = dist(xC, yC, xA, yA);

    double max_len = max({ab, bc, ca});
    double min_len = min({ab, bc, ca});

    double result = 2.0 * (max_len - min_len);

    cout << fixed << setprecision(10) << result << "\n";

    return 0;
}