#include <iostream>
#include <string>

using namespace std;

int countZeros(int n) {
    if (n == 0) return 1;
    
    int count = 0;
    while (n > 0) {
        if (n % 10 == 0) {
            count++;
        }
        n /= 10;
    }
    return count;
}

int main() {
    int T;
    cin >> T;

    while (T--) {
        int N, M;
        cin >> N >> M;

        int result = 0;
        for (long long i = N; i <= M; ++i) {
            result += countZeros(i);
        }
        
        cout << result << "\n";
    }

    return 0;
}