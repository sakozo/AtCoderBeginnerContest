#include <bits/stdc++.h>
using namespace std;

int main() {
    double a;
    cin >> a;

    double a1 = a;

    double count = 0;

    for(int i=a;i>0;i--){
        if(i%2 != 0){
            count++;
        }
    }

    double ans = count/a1;

    cout << ans << endl;
}
