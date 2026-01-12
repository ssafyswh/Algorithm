#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> tree(N);
    for (int i = 0; i < N; i++) {
        cin >> tree[i]; 
    }
    sort(tree.begin(), tree.end(), greater<int>());
    int result = 0;
    for (int i = 0; i < N; i++) {
        int fin = tree[i] + (i + 1) + 1;
        if (result < fin) result = fin;
    }
    cout << result;
    return 0;
}