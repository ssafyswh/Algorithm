#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Dish {
    long long T, A, B;
};

int main() {
    int N;
    long long D;
    cin >> N >> D;

    vector<Dish> dishes(N);
    long long max_score = 0;

    for (int i = 0; i < N; i++) {
        cin >> dishes[i].T >> dishes[i].A >> dishes[i].B;
        max_score = max(max_score, dishes[i].A + dishes[i].B);
    }

    sort(dishes.begin(), dishes.end(), [](const Dish& d1, const Dish& d2) {
        return d1.T < d2.T;
    });

    vector<long long> prefA(N);
    vector<long long> times(N);
    
    prefA[0] = dishes[0].A;
    times[0] = dishes[0].T;

    for (int i = 1; i < N; i++) {
        prefA[i] = max(prefA[i - 1], dishes[i].A);
        times[i] = dishes[i].T;
    }

    for (int j = 0; j < N; j++) {
        long long remain_time = D - dishes[j].T;
        
        if (remain_time < 1) continue;

        auto it = upper_bound(times.begin(), times.end(), remain_time);
        
        if (it != times.begin()) {
            int k = distance(times.begin(), it) - 1;
            max_score = max(max_score, prefA[k] + dishes[j].B);
        }
    }

    cout << max_score << "\n";

    return 0;
}