#include <iostream>
#include <string>

using namespace std;

int main() {
    int N;
    cin >> N;
    N--;
    string first_command;
    cin >> first_command;
    string result = first_command;
    int L = result.size();
    while (N--) {
        string command;
        cin >> command;
        for (int i = 0; i < L; i++) {
            if (command[i] != result[i]) result[i] = '?';
        }
    }
    cout << result;
}