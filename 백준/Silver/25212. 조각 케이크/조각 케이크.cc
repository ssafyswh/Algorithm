#include <iostream>
#include <vector>

using namespace std;

int N;
int result = 0;
vector<double> cakes;

void whole(int n, double sum) {
    if (n == N) {
        if (sum >= 0.99 && sum <= 1.01) result++;
        return;
    }
    double cake = 1 / cakes[n];
    whole(n + 1, sum + cake);
    whole(n + 1, sum);
}

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        double cake;
        cin >> cake;
        cakes.push_back(cake);
    }
    whole(0, 0.0);
    cout << result;
    return 0;
}