#include <bits/stdc++.h>
using namespace std;
 
int main() {
    string S;
    cin >> S;
    int n = S.size();

    int ans = 0;
    int r = n/2;
    for(int i=0;i<r;i++){
      if(S.at(i)!=S.at(n-1-i)){
       ans++;
       //cout << i <<endl;
      }
      //ans++;
    }
    cout << ans << endl;
}