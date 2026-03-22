#include <iostream>
#include <deque>
#include <vector>

using namespace std;

int main() {
    int N, Q, C;
    cin >> N >> Q >> C;

    vector<int> CAP(N + 1);
    for (int i = 1; i <= N; ++i) cin >> CAP[i];

    deque<int> b_space, f_space;
    int cur = 0, cache = 0;

    while (Q--) {
        char op;
        cin >> op;

        if (op == 'B' && !b_space.empty()) {
            f_space.push_back(cur);
            cur = b_space.back();
            b_space.pop_back();
        } 
        else if (op == 'F' && !f_space.empty()) {
            b_space.push_back(cur);
            cur = f_space.back();
            f_space.pop_back();
        } 
        else if (op == 'A') {
            int p;
            cin >> p;
            while (!f_space.empty()) {
                cache -= CAP[f_space.back()];
                f_space.pop_back();
            }
            if (cur) b_space.push_back(cur);
            cur = p;
            cache += CAP[p];
            while (cache > C && !b_space.empty()) {
                cache -= CAP[b_space.front()];
                b_space.pop_front();
            }
        } 
        else if (op == 'C' && !b_space.empty()) {
            deque<int> temp;
            for (int p : b_space) {
                if (temp.empty() || temp.back() != p) temp.push_back(p);
                else cache -= CAP[p];
            }
            b_space = temp;
        }
    }

    cout << cur << "\n";
    
    auto print_dq = [](deque<int>& dq) {
        if (dq.empty()) cout << "-1\n";
        else {
            for (auto it = dq.rbegin(); it != dq.rend(); ++it) cout << *it << " ";
            cout << "\n";
        }
    };
    
    print_dq(b_space);
    print_dq(f_space);

    return 0;
}