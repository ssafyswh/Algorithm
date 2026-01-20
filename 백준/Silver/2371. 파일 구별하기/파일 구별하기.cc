#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;
    int result = 1;
    vector<vector<int>> files(N);
    for (int n = 0; n < N; n++) {
        vector<int> file;
        while (true) {
            int num;
            cin >> num;
            if (num == -1) break;
            file.push_back(num);
        }
        files[n] = file;
        for (int i = 0; i < n; i++) {
            vector<int> file2 = files[i];
            int len = min(file.size(), file2.size());
            int cnt = 1;
            for (int j = 0; j < len; j++) {
                if (file[j] == file2[j]) {
                    cnt++;
                } else break;
            }
            result = max(result, cnt);
        }
    }
    cout << result;
    return 0;
}