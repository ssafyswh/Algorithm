#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main() {
    map<int, int> order;
    vector<int> score(9);
    for (int i = 1; i < 9; i++) {
        int n;
        cin >> n;
        order[n] = i;
        score[i] = n;
    }
    sort(score.begin(), score.end(), greater<int>());
    int sum = 0;
    vector<int> result;
    for (int i = 0; i < 5; i++) {
        sum += score[i];
        result.push_back(order[score[i]]);
    }
    sort(result.begin(), result.end());
    cout << sum << "\n";
    for (int num : result) cout << num << " ";
    return 0; 
}