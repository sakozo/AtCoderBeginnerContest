#include <bits/stdc++.h>
using namespace std;
 
int main() {
    string b;
    cin >> b;
    string ans;
    if(b=="SUN"){
      ans = "7";
    }else if(b=="MON"){
      ans = "6";
    }else if(b=="TUE"){
      ans = "5";
    }else if(b=="WED"){
      ans = "4";
    }else if(b=="THU"){
      ans = "3";
    }else if(b=="FRI"){
      ans = "2";
    }else if(b=="SAT"){
      ans = "1";
    }
    cout << ans << endl;
}