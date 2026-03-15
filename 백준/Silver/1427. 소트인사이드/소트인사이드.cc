#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

char ord[10] = {'9', '8', '7', '6', '5', '4', '3', '2', '1', '0'};

int main() {
    string num;
    cin >> num;
    unordered_map<char, int> cnt;
    for (char digit : num) {
        cnt[digit]++;
    }
    for (char digit : ord) {
        for (int i = 0; i < cnt[digit]; i++) {
            cout << digit;
        }
    }
    return 0;
}