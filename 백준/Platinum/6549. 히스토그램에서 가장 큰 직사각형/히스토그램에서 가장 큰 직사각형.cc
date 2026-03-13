#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main() {
    while (true) {
        int N;
        cin >> N;
        if (N == 0) break;
        vector<int> histogram(N + 1, 0);
        for (int i = 0; i < N; i++) cin >> histogram[i];

        long long result = 0;
        stack<int> s;
        for (int i = 0; i < N + 1; i++) {
            while (!s.empty() && histogram[s.top()] > histogram[i]) {
                int idx1 = s.top();
                int height = histogram[idx1];
                s.pop();
                int width;
                if (s.empty()) width = i;
                else width = i - s.top() - 1;
                result = max(result, (long long)height * width);
            }
            s.push(i);
        }
        cout << result << "\n";
    }

    return 0;
}