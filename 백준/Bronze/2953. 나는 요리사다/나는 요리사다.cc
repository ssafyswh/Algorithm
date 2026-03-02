#include <iostream>
#include <string>

using namespace std;

int main() {
    int win_order, win_score = 0;
    for (int i = 1; i < 6; i++) {
        int sum = 0;
        for (int j = 0; j < 4; j++) {
            int score;
            cin >> score;
            sum += score;
        }
        if (sum > win_score) {
            win_score = sum;
            win_order = i;
        }
    }
    cout << win_order << " " << win_score;
    return 0;
}