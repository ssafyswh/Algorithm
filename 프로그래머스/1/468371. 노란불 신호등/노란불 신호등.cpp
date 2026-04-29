#include <vector>
#include <numeric>

using namespace std;

int solution(vector<vector<int>> signals) {
    int n = signals.size();
    int time_limit = 1;
    vector<int> S(n);
    vector<int> Y(n);
    for (int i = 0; i < n; i++) {
        S[i] = signals[i][0] + signals[i][1] + signals[i][2];
        Y[i] = signals[i][0] + signals[i][1];
        time_limit = lcm(time_limit, S[i]);
    }
    time_limit++;
    
    int time = 0;
    while (time <= time_limit) {
        time++;
        bool exist_answer = true;
        for (int i = 0; i < n; i++) {
            int now = time % S[i];
            if (now <= Y[i] && now > signals[i][0]) continue;
            exist_answer = false;
            break;
        }
        if (exist_answer) return time;
    }
    return -1;
}