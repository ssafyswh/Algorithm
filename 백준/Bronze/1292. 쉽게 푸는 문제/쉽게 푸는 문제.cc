#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

vector<int> series = {0};

int main() {
    int a, b;
    cin >> a >> b;
    int n = 0;
    while (series.size() <= 1001) {
        n++;
        for (int i = 0; i < n; i++) {
            series.push_back(n);
        }
    }
    int result = accumulate(series.begin() + a, series.begin() + b + 1, 0);
    cout << result;
    return 0;
}