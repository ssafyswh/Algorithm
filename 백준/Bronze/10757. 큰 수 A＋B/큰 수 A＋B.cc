#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string addBigInt(string n1, string n2) {
    string result = "";
    int sum = 0;
    int i = n1.size() - 1;
    int j = n2.size() - 1;

    while (i >= 0 || j >= 0 || sum > 0) {
        if (i >= 0) sum += n1[i--] - '0';
        if (j >= 0) sum += n2[j--] - '0';
        result += (sum % 10) + '0'; 
        sum /= 10;
    }
    reverse(result.begin(), result.end());
    return result;
}

int main() {
    string a, b;
    if (cin >> a >> b) {
        cout << addBigInt(a, b) << "\n";
    }
    return 0;
}