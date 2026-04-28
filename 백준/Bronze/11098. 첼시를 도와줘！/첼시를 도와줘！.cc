#include <iostream>
#include <string>

using namespace std;
int main() {
    int n;
    cin >> n;
    for (int t = 0; t < n; t++) {
        int p;
        cin >> p;
        int max_value = 0;
        string result;
        for (int i = 0; i < p; i++) {
            int C; string name;
            cin >> C >> name;
            if (max_value < C) {
                max_value = C;
                result = name;
            }
        }
        cout << result << "\n";
    }
}