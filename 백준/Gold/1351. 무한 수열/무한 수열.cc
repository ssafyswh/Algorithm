#include <iostream>
#include <unordered_map>

using namespace std;

long long P, Q;
unordered_map<long long, long long> memo;

long long solve(long long n) {
    if (n == 0) return 1;
    if (memo.count(n)) return memo[n];
    return memo[n] = solve(n / P) + solve(n / Q);
}

int main() {
    long long N;
    cin >> N >> P >> Q;
    cout << solve(N);
    return 0;
}