#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    vector<pair<int, string>> words(N);
    for (int i = 0; i < N; i++) {
        cin >> words[i].second >> words[i].first;
    }
    sort(words.begin(), words.end());

    vector<vector<string>> result(4);

    for (int i = 0; i < N; i++) {
        result[i % 4].push_back(words[i].second);
    }
    
    for (int i = 0; i < 4; i++) {
        sort(result[i].begin(), result[i].end());
        cout << i + 1;
        for (const string& word : result[i]) cout << " " << word;
        cout << "\n";
    }

    return 0; 
}