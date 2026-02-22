#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int nA, nB;
    cin >> nA >> nB;

    vector<int> A(nA);
    for (int i = 0; i < nA; i++) {
        cin >> A[i];
    }
    sort(A.begin(), A.end());
    int intersection_count = 0;
    
    for (int i = 0; i < nB; i++) {
        int b_val;
        cin >> b_val; 
        if (binary_search(A.begin(), A.end(), b_val)) {
            intersection_count++;
        }
    }
    int answer = (nA - intersection_count) + (nB - intersection_count);
    cout << answer << "\n";

    return 0;
}