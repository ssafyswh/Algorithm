#include <iostream>

using namespace std;

int main() {
    int T; 
    cin >> T;
    for (int case_num = 1; case_num <= T; ++case_num) {
        int a, b;
        cin >> a >> b;

        int sum = a + b;
        
        cout << "Case #" << case_num << ": " << a << " + " << b << " = " << sum << "\n";
    }

    return 0;
}