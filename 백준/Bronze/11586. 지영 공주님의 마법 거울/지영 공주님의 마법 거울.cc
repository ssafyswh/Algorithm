#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<string> mirror(N);
    for (int i = 0; i < N; i++) cin >> mirror[i];

    int mood;
    cin >> mood;
    if (mood == 2) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N / 2; j++) {
                swap(mirror[i][j], mirror[i][N - j - 1]);
            }
        }
    } else if (mood == 3) {
        for (int i = 0; i < N / 2; i++) swap(mirror[i], mirror[N - i - 1]);
    }
    for (string row : mirror) cout << row << "\n";
    return 0; 
}