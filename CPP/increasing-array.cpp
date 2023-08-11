#include <bits/stdc++.h>

using namespace std;


#define ll long long
int main() 
{
    int n;
    cin >> n;
    int mx =0;
    ll ans=0; 
    for (int i = 0; i < n; i++)
    {
        int x; 
        cin >> x;
        mx = max(mx, x);
        ans +=mx -x;
        //keep track of the maximum number so far
    }
    cout << ans;
}

/* 
5
3 2 5 1 7
5

...Program finished with exit code 0
Press ENTER to exit console.


*/
