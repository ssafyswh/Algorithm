#include <iostream>
#include <string>

using namespace std;

int main() {
    string board;
    cin >> board;

    size_t pos = 0;
    while ((pos = board.find("XXXX", pos)) != string::npos) {
        board.replace(pos, 4, "AAAA");
        pos += 4;
    }

    pos = 0;
    while ((pos = board.find("XX", pos)) != string::npos) {
        board.replace(pos, 2, "BB");
        pos += 2;
    }

    if (board.find('X') != string::npos) {
        cout << -1;
    } else {
        cout << board;
    }

    return 0;
}