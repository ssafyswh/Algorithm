#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

int main() {
    int N;
    cin >> N;
    string first_student;
    cin >> first_student;
    int L = first_student.size();
    reverse(first_student.begin(), first_student.end());
    vector<unordered_set<string>> ids(L + 1);
    for (int l = 1; l <= L; l++) {
        ids[l].insert(first_student.substr(0, l));
    }

    for (int i = 1; i < N; i++) {
        string student;
        cin >> student;
        reverse(student.begin(), student.end());
        for (int l = 1; l <= L; l++) {
            ids[l].insert(student.substr(0, l));
        }
    }

    int result = L;
    for (int i = L - 1; i > 0; i--) {
        if (ids[i].size() == N) {
            result = i;
        }
    }
    cout << result;
    return 0;
}