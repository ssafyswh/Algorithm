#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    int N;
    if (!(cin >> N)) return 0;

    for (int i = 0; i < N; ++i) {
        double a, b;
        if (!(cin >> a >> b)) break;

        double result = a * 2.0 / b;

        cout << "The height of the triangle is " << fixed << setprecision(2) << result << " units" << endl;
    }

    return 0;
}