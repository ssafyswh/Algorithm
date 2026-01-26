#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Element {
    int value;
    int original_idx;
};

bool compare(const Element& a, const Element& b) {
    if (a.value == b.value) {
        return a.original_idx < b.original_idx;
    }
    return a.value < b.value;
}

int main() {
    int N;
    cin >> N;
    vector<Element> A(N);
    vector<int> P(N);

    for (int i = 0; i < N; i++) {
        cin >> A[i].value;
        A[i].original_idx = i;
    }

    sort(A.begin(), A.end(), compare);

    for (int j = 0; j < N; j++) {
        P[A[j].original_idx] = j;
    }
    for (int i = 0; i < N; i++) {
        cout << P[i] << " ";
    }

    return 0;
}