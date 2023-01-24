#include <iostream>
using namespace std;
int main()
{
    int a, b, n, c, s;
    a = -1;
    b = 1;
    s = 0;
    cout << "enter n: ";
    cin >> n;

    while (s != n)
    {
        c = a + b;
        cout << c << "\n";
        a = b;
        b = c;
        s++;
    }
    return 0;
}