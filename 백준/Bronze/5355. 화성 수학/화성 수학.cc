#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    if (!(cin >> T)) return 0;
    cin.ignore();

    while (T--) {
        string line;
        getline(cin, line);
        
        stringstream ss(line);
        double num;
        ss >> num;

        string oper;
        while (ss >> oper) {
            if (oper == "@") {
                num *= 3;
            } else if (oper == "%") {
                num += 5;
            } else if (oper == "#") {
                num -= 7;
            }
        }

        cout << fixed << setprecision(2) << num << "\n";
    }
    return 0;
}