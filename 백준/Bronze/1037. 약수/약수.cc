#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
    int n;
    cin >> n;
    vector<int> div(n, 0);
    for (int i = 0; i < n; i++) {
        cin >> div[i];
    }
    sort(div.begin(), div.end());
    int result = div[0] * div[n - 1];
    cout << result;
    return 0;
}