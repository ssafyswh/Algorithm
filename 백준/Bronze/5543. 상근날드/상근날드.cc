#include <iostream>

using namespace std;

int main() {
    int burger = 2100;
    for (int i = 0; i < 3; i++) {
        int cost;
        cin >> cost;
        burger = min(burger, cost);
    }

    int drink = 2100;
    for (int i = 0; i < 2; i++) {
        int cost;
        cin >> cost;
        drink = min(drink, cost);
    }
    cout << (burger + drink) - 50;
    return 0; 
}