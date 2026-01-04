#include <iostream>
#include <string>

using std::cin;
using std::cout;

int main()
{
    int V;
    cin >> V;
    int countA = 0; int countB = 0;
    std::string votes;
    cin >> votes;
    for (int i = 0; i < votes.length(); i++) {
        char vote = votes[i];
        if (vote == 'A') countA++;
        else countB++;
    }
    if (countA > countB) cout << "A";
    else if (countA == countB) cout << "Tie";
    else cout << "B";
    return 0;
}