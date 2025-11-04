#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int M, N;
    cin >> M >> N;

    int sum = 0;
    int min_square = 0;

    for (int i = M; i <= N; i++) {
        int root = (int)sqrt(i);
        if (root * root == i) { 
            sum += i;
            if (min_square == 0) {
                min_square = i;
            }
        }
    }

    if (sum == 0) {
        cout << -1 << endl;
    } else {
        cout << sum << endl;
        cout << min_square << endl;
    }

    return 0;
}
