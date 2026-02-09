#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {
    priority_queue<long long, vector<long long>, greater<long long>> deck;
    long long n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        deck.push(num);
    }
    for (int i = 0; i < m; i++) {
        long long a = deck.top();
        deck.pop();
        long long b = deck.top();
        deck.pop();
        deck.push(a + b);
        deck.push(a + b);
    }
    long long result = 0;
    for (int i = 0; i < n; i++) {
        result += deck.top();
        deck.pop();
    }
    cout << result;
    return 0;
}