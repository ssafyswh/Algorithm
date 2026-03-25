#include <iostream>
#include <string>

using namespace std;

char base[4] = {'A', 'C', 'G', 'T'};
int cnt[4] = {0, 0, 0, 0};

int main() {
    int n;
    string dna;
    cin >> n >> dna;
    for (char b : dna) {
        switch (b) {
            case 'A': cnt[0]++; break;
            case 'C': cnt[1]++; break; 
            case 'G': cnt[2]++; break;
            case 'T': cnt[3]++; break;
        }
    }
    int min_value = n + 1;
    int min_idx = -1;
    for (int i = 0; i < 4; i++) {
        if (min_value > cnt[i]) {
            min_value = cnt[i];
            min_idx = i;
        }
    }
    cout << min_value << "\n";
    for (int i = 0; i < n; i++) cout << base[min_idx];
    return 0;
}