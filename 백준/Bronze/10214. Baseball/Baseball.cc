#include <iostream>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        int yonsei = 0;
        int korea = 0;
        for (int j = 0; j < 9; j++)
        {
            int y, k;
            cin >> y >> k;
            yonsei += y;
            korea += k;
        }
        if (yonsei > korea)
        {
            cout << "Yonsei";
        }
        else if (yonsei == korea)
        {
            cout << "Draw";
        }
        else
        {
            cout << "Korea";
        }
        cout << "\n";
    }
    return 0;
}