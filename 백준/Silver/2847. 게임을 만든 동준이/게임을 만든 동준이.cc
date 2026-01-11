#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N;
    cin >> N;
    vector<int> level(N);
    for (int i = 0; i < N; i++) {
        cin >> level[i];
    }
    int result = 0, highest = level[N - 1]; 
    for (int i = N - 2; i >= 0; i--) {
        if (level[i] >= highest) {
            result += (level[i] - (highest - 1));
            level[i] = highest - 1;
        }
        highest = level[i];
    }
    cout << result << "\n";
    
    return 0;
}