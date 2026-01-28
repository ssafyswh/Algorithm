#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
    int N1, N2;
    cin >> N1 >> N2;
    string group1, group2;
    cin >> group1 >> group2;
    int T;
    cin >> T;
    reverse(group1.begin(), group1.end());
    string result = group1 + group2;
    while (T--) {
        for (int i = 1; i < N1 + N2; i++) {
            if (group1.find(result[i - 1]) != string::npos && group2.find(result[i]) != string::npos){
                swap(result[i - 1], result[i]);
                i++;
            } 
        }
    }
    
    cout << result;
    return 0;
}