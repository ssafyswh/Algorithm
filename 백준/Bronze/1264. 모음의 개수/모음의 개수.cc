#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

unordered_set<char> vowel = {'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'};

int main() {
    while (true) {
        string line;
        getline(cin, line);
        if (line == "#") break;
        int result = 0;
        for (char a : line) {
            if (vowel.count(a) == 1) result++;
        }
        cout << result << "\n";
    }
    return 0;
}