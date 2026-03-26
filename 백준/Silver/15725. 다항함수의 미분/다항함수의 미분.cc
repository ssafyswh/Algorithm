#include <iostream>
#include <string>

using namespace std;

int main() {
    string oper;
    cin >> oper;
    string result = "";
    bool has_var = false;
    for (char a : oper) {
        if (a == 'x') {
            has_var = true;
            break;
        }
        result += a;
    }
    if (has_var) {
        if (result == "") cout << 1;
        else if (result == "-") cout << -1;
        else cout << result;
    } else cout << 0;
    return 0;
}