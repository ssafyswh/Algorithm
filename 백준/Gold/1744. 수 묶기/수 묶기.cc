#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> positive, negative;
    int zero = 0;
    for (int i = 0; i < N; i++) {
        int num;
        cin >> num;
        if (num > 0) positive.push_back(num);
        else if (num == 0) zero ++;
        else negative.push_back(num);
    }
    sort(positive.begin(), positive.end(), greater<int>());
    sort(negative.begin(), negative.end());
    int result = 0;
    int len_p = positive.size();
    for (int i = 0; i < len_p / 2; i++) {
        int num1 = positive[2 * i], num2 = positive[2 * i + 1];
        if (num1 != 1 && num2 != 1) result += num1 * num2;
        else result += num1 + num2;
    }
    if (len_p % 2 == 1) result += positive[len_p - 1];
    int len_n = negative.size();
    for (int i = 0; i < len_n / 2; i++) {
        int num1 = negative[2 * i], num2 = negative[2 * i + 1];
        result += num1 * num2;
    }
    if (len_n % 2 == 1 && zero == 0) result += negative[len_n - 1];
    cout << result;
    return 0;
}