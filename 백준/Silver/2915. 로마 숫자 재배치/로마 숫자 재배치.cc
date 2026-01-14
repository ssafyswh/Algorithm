#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

unordered_map<char, int> cnt = {
    {'I', 0},
    {'V', 0},
    {'L', 0},
    {'C', 0},
};

unordered_map<int, string> rome = {
    {1, "I"},
    {2, "II"},
    {3, "III"},
    {4, "IV"},
    {5, "V"},
    {6, "VI"},
    {7, "VII"},
    {8, "VIII"},
    {9, "IX"},
    {10, "X"},
    {20, "XX"},
    {30, "XXX"},
    {40, "XL"},
    {50, "L"},
    {60, "LX"},
    {70, "LXX"},
    {80, "LXXX"},
    {90, "XC"},
};

int main() {
    string B;
    cin >> B;
    int result = 0;
    for (char digit : B) {
        cnt[digit]++;
    };
    if (cnt['C'] == 1) {
        cnt['C']--;
        cnt['X']--;
        result += 90;
    }
    if (cnt['L'] == 1) {
        if (cnt['X'] == 1) {
            cnt['L']--;
            cnt['X']--;
            result += 40;
        } else if (cnt['X'] == 2 && cnt['I'] == 1 && cnt['V'] == 0){
            cnt['L']--;
            cnt['X'] = 0;
            cnt['I']--;
            result += 49;
        }
    }
    if (cnt['X'] > 0 && cnt['I'] == 1) {
        cnt['X']--;
        cnt['I']--;
        result += 9;
    }
    if (cnt['V'] == 1 && cnt['I'] == 1) {
        cnt['V']--;
        cnt['I']--;
        result += 4;
    }
    result += cnt['I'] + cnt['V'] * 5 + cnt['X'] * 10 + cnt['L'] * 50;
    int ten = result / 10, one = result % 10;  
    if (ten != 0) cout << rome[ten * 10];
    if (one != 0) cout << rome[one];
    return 0;
}