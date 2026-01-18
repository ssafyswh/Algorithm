#include <iostream>
#include <string>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        int max_alcohol = 0;
        string result;
        for (int n = 0; n < N; n++) {
            string university;
            int alcohol;
            cin >> university >> alcohol;
            if (max_alcohol <= alcohol) {
                result = university;
                max_alcohol = alcohol;
            }
        }
        cout << result << "\n";
    }
    return 0;
}