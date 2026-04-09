#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> series(N + 1);
    for (int i = 1; i < N + 1; i++) cin >> series[i];
    
    int M;
    cin >> M;
    while (M--) {
        int L, R;
        cin >> L >> R;
        int cnt = L;
        for (int i = 1; i < N + 1; i++) {
            int num = series[i];
            if (num >= L && num <= R) {
                cout << cnt << " ";
                cnt++;
            }
            else cout << num << " ";
        }
        cout << "\n";
    }
    return 0; 
}